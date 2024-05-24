
import os
import json
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from src.tools.email.email_functions import send_email
from src.tools.tool import Tool



class EmailInput(BaseModel):
    receiver_email : str = Field(description="The email address of the recipient")
    body : str = Field(description="The body of the email to be sent")

def send_email_(receiver_email : str, body : str) -> str:
    """Tool to send an email."""
    status = send_email(receiver_email=receiver_email, body = body)
    return status

def send_email_executor(args):
    return send_email_(args["receiver_email"], args["body"])


class EmailTool(Tool):
    def __init__(self, input_schema=EmailInput, func=send_email_, 
                 executor=send_email_executor) -> None:
        super().__init__(input_schema, func, executor)


