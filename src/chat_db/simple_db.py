import os
from src.config import SYSTEM
from src.logger import logging


class SimpleChatDB:
    def __init__(self) -> None:
        self.db = dict()  # {"phone"  : "history : list of messages "}
        self.available_phone_numbers = list()

    def add_new_number(self, phone_number:str, user_name = "not given"):
        """Adds new phone number to the database and initialises the history.

        Args:
            phone_number (str): phone number to add
        """

        self.db[phone_number] = self.init_history(user_name)
        self.available_phone_numbers.append(phone_number)
        logging.info(f"{phone_number} added successfully to the database.")

    def init_history(self, user_name):
        """Initialises the history with a system message. 
        """
        message = [{
            "role": "system",
            "content": SYSTEM.format(user_name=user_name),
            }]
        logging.info(f"New history initialized.")
        return message

    def retrieve_history(self, phone_number):
        return self.db[phone_number]
    
    def update_history(self, phone_number , history: list[dict]):
        self.db[phone_number] = history
        logging.info(f"History updated successfully.")

    def renew_history(self, phone_number, user_name="not given") : 
        self.db[phone_number] = self.init_history(user_name)




