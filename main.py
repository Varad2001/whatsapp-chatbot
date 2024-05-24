import os
from flask import Flask, jsonify, request
from src.connectors.whatsapp.whatsapp_api import send_message
from src.llm.llms import LLM
from src.tools import Tools



if __name__ == '__main__':

    tools = Tools()
    llm = LLM(tools=tools)
    
    while True:
        q = input("Query : ")
        if q.strip() == "stop":
            break
        response = llm.chat(q)
        print(response)
        print()


