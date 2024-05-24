import json
import inspect
from pydantic import BaseModel


def generate_tool_description(func, input_model: BaseModel):
    """Generate a tool description JSON for a given function."""
    
    signature = inspect.signature(func)
    func_doc = func.__doc__ if func.__doc__ else f"Function to {func.__name__}"
    
    desc = input_model.model_json_schema()["properties"]
    properties = {}
    for param, d in desc.items():
         properties[param] = {
              "type" : d["type"],
              "description" : d["description"]
         }
        

    tool_description = {
        "type": "function",
        "function": {
            "name": func.__name__,
            "description": func_doc,
            "parameters": {
                "type": "object",
                "properties": properties
            },
             "required": list(properties.keys()),
        }
    }

    
    return tool_description