
import os
import json
import requests
from pydantic import BaseModel, Field
from src.tools.tool import Tool
from src.config import WEATHER_API_KEY, WEATHER_API_CALL


class InputGetweather(BaseModel):
    location : str = Field(description="The city name to check the weather. e.g. Pune, London, Indore, etc.")

def get_current_weather(location:str)-> str:
    """Get the weather at the given location. Share only relevant, simple details to the user. \
        Like temperature, humidity, cloud cover, etc. Only if the user asks for more details, then \
            share complicated details like Pressure, UV Index, etc."""
    response = requests.get(WEATHER_API_CALL.format(key=WEATHER_API_KEY, location=location))
    return response.json()

def get_current_weather_executor(args):
    return get_current_weather(args["location"])

class GetWeatherTool(Tool):
    def __init__(self, input_schema=InputGetweather, func=get_current_weather, 
                 executor=get_current_weather_executor) -> None:
        super().__init__(input_schema, func, executor)




