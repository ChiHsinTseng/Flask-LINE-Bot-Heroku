from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)


line_bot_api = LineBotApi('Zt18oeL1jEzB9bbOw3BjRbMC9u8q4FwJkV2J7wlRd9G+GY5D8HHrShTSGZRK7uIKTAbqmImphpl3/U2G2B3wFLshfMnvqVCsZW+lWZrxUT3XOMma0KcbeLxwc9v7DdTbtRyi/UedtsR7jJE3NSquLQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('18a7d98e70f62d369081d4d82c88a1e3')

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
       abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    #print(type(msg))
    msg = msg.encode('utf-8')  
    if event.message.text == "文字":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
