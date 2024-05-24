import os
from src.utils import generate_tool_description



class Tool:
    def __init__(self, input_schema, func, executor) -> None:
        self.input_schema = input_schema
        self.func = func
        self.executor = executor
        self.tool_name = self.func.__name__

        self.get_description()

    def get_description(self):
        self.tool_description = generate_tool_description(
            func=self.func,
            input_model=self.input_schema
        )



