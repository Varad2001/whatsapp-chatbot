import os
from src.tools.weather.weather_tool import GetWeatherTool
from src.tools.email.email_tool import EmailTool
from src.tools.calculator.multiply_tool import MultiplyTool


available_tools = [GetWeatherTool(), EmailTool(), MultiplyTool()]

class Tools:
    
    def __init__(self):
        self.available_tools  = available_tools
        self.tool_to_call = dict()

        self.get_tools_info()

    def get_tools_info(self):
        tools_json = list()
        for tool in self.available_tools:
            tools_json.append(tool.tool_description)
            self.tool_to_call[tool.tool_name] = tool.executor
        self.tools_meta_data = tools_json


