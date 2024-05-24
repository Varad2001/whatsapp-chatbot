

import os
import json
from pydantic import BaseModel, Field
from src.tools.tool import Tool


class InputGetweather(BaseModel):
    location : str = Field(description="The location to check the weather.")

def get_current_weather(location:str)-> str:
    """Get the weather at the given location."""
    return "{ 'temperature': '33 degree', 'type':'sunny'}"

def get_current_weather_executor(args):
    return get_current_weather(args["location"])

class GetWeatherTool(Tool):
    def __init__(self, input_schema=InputGetweather, func=get_current_weather, 
                 executor=get_current_weather_executor) -> None:
        super().__init__(input_schema, func, executor)




