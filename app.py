import os
from flask import Flask, jsonify, request
from src.connectors.whatsapp.whatsapp_api import send_message
from src.llm.llms import LLM
from src.tools import Tools


app = Flask(__name__)

llm = LLM(Tools())
NEW_SESSION = "/new"

@app.route('/message', methods=['GET', "POST"])
def message():
    if request.method=="POST":
        data = request.form
        from_number = str(data["From"]).split(":")[-1]
        if data["Body"].strip()==NEW_SESSION:
            llm.init_history()
            send_message(to_number=from_number, body_text="New history initialized.")
            return jsonify("New history initialized.")
        input_query = f"""ProfileName : {data["ProfileName"]} \n \
        Text message : {data["Body"]}"""
        response = llm.chat(query=input_query)
        send_message(to_number=from_number, body_text=response)
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
