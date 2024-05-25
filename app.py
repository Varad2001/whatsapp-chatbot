import os
from flask import Flask, jsonify, request
from src.connectors.whatsapp.whatsapp_api import send_message
from src.llm.llms import LLM
from src.tools import Tools
from src.chat_db.simple_db import SimpleChatDB


app = Flask(__name__)

llm = LLM(Tools())
db = SimpleChatDB()
NEW_SESSION = "/new"

@app.route('/message', methods=['GET', "POST"])
def message():
    if request.method=="POST":
        data = request.form
        from_number = str(data["From"]).split(":")[-1]

        # check if the number is already in the database
        if not from_number in db.available_phone_numbers:
            db.add_new_number(phone_number=from_number)

        if data["Body"].strip()==NEW_SESSION:
            db.renew_history(from_number)
            send_message(to_number=from_number, body_text="New history initialized.")
            return jsonify("New history initialized.")
        

        input_query = f"""ProfileName : {data["ProfileName"]} \n \
        Text message : {data["Body"]}"""

        # get response : pass history of the respective number
        response = llm.chat(query=input_query, history=db.retrieve_history(from_number))

        # get the new history and save it
        new_history = llm.messages
        db.update_history(phone_number=from_number, history=new_history)

        
        send_message(to_number=from_number, body_text=response)
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
