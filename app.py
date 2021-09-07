import os
import requests
from datetime import datetime,date,timezone,timedelta

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text
    # Send To Line
    #response = requests.post('https://ncutcbpapi.ncut.edu.tw/api/login', json={"userId":"A0401","password":"04850"})
    #response_Json = response.json()
    #API = "https://ncutcbpapi.ncut.edu.tw/api/codes/A0401/"+ datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
    #TOKEN = "bearer "+response_Json['token']
    #r=requests.get(API, headers={"authorization":TOKEN})
    reply = TextSendMessage(text=f"{TEST}")
    line_bot_api.reply_message(event.reply_token, reply)