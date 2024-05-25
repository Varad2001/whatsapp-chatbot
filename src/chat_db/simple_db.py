import os
from src.config import SYSTEM


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

    def init_history(self, user_name):
        """Initialises the history with a system message. 
        """
        message = [{
            "role": "system",
            "content": SYSTEM.format(user_name=user_name),
            }]
        return message

    def retrieve_history(self, phone_number):
        return self.db[phone_number]
    
    def update_history(self, phone_number , history: list[dict]):
        self.db[phone_number] = history

    def renew_history(self, phone_number, user_name="not given") : 
        self.db[phone_number] = self.init_history(user_name)




