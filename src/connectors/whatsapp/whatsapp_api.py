# Standard library import
import os
from dotenv import load_dotenv
from src.logger import logging
from src.config import account_sid, auth_token, client , twilio_number


# Sending message logic through Twilio Messaging API
def send_message(to_number, body_text):
    try:
        message = client.messages.create(
            from_=f"whatsapp:{twilio_number}",
            body=body_text,
            to=f"whatsapp:{to_number}"
            )
        logging.info(f"Message sent to {to_number}: {message.body}")
    except Exception as e:
        logging.error(f"Error sending message to {to_number}: {e}")

if __name__ == "__main__":
    send_message(to_number="+919175373448", body_text="heello")