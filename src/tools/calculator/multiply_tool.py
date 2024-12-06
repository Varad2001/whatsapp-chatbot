
import os
import json
from pydantic import BaseModel, Field
from src.tools.tool import Tool


class InputMultiply(BaseModel):
    num_1 : int = Field(description="First number in multiplication")
    num_2 : int = Field(description="Second number in multiplication")

def multiply(num_1 : int, num_2: int)-> int:
    """Multiply two given integers."""
    return int(num_1) * int(num_2)

def multiply_executor(args):
    return multiply(args["num_1"] , args["num_2"])

class MultiplyTool(Tool):
    def __init__(self, input_schema=InputMultiply, func=multiply, 
                 executor=multiply_executor) -> None:
        super().__init__(input_schema, func, executor)




