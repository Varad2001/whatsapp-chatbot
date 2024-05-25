import os
from twilio.rest import Client


############### LLM config  #####################
MAX_ITERATIONS = 15

BASE_URL = "https://proxy.tune.app/"
TUNESTUDIO_KEY = os.environ.get("TUNESTUDIO_API_KEY")
MODEL_NAME = "rohan/tune-gpt-4o"
#MODEL_NAME = "gpt-3.5-turbo"

SYSTEM = "You are an AI assistant deployed to answer user questions through WhatsApp. \
    When using tools, THINK STEP BY STEP, STRICTLY CALL ONE TOOL AT A TIME. \
     Use Whatsapp formatting. Also make use of proper emojis when possible. \
        \n Some details : \n Name of the user : {user_name}"


############### twilio credentials  #####################
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
twilio_number = os.environ.get('TWILIO_NUMBER')



############### Email credentials  #####################
EMAIL = 'vktesting4@gmail.com'
PASSWORD = os.environ.get("SENDER_PASSWORD")
IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

############### WEATHER API credentials  #####################
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
WEATHER_API_CALL = "http://api.weatherapi.com/v1/current.json?key={key}&q={location}"
