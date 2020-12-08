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

    
    if event.message.text == "拉麵推薦":       
        buttons_template1 = TemplateSendMessage(
        alt_text='你想吃哪裡的拉麵？',
        template=ButtonsTemplate(
            title='你想吃哪裡的拉麵？',
            text='最好選近的不然你會餓死',
            thumbnail_image_url='https://1.bp.blogspot.com/-ZWe-zRa3stE/XlTGFl7NksI/AAAAAAAAvmY/fR_RrfO6GAYdQSirnCC-bqvelI7LkUnYwCEwYBhgL/s1600/ACA5ABA1-3DDE-4042-8205-2572D5AFD0B5.JPG',
            actions=[
                MessageTemplateAction(
                    label='北部',
                    text='北部'
                ),
                 MessageTemplateAction(
                    label='中部',
                    text='中部'
                ),
                MessageTemplateAction(
                    label='南部',
                    text='南部'
                ),
                MessageTemplateAction(
                    label='東部',
                    text='東部'
                ),  

            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template1)
 


    elif event.message.text == "錯誤回報":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "請點選以下連結：https://reurl.cc/14RmVW"))

        
        
    elif event.message.text == "北部":       
        buttons_template2 = TemplateSendMessage(
        alt_text='你在哪個縣市？',
        template=ButtonsTemplate(
            title='你在哪個縣市？',
            text='讓我知道你在哪個縣市會加速我找到適合的店喔！',
            #image_background_color = 9B9B7A,
            thumbnail_image_url='https://1.bp.blogspot.com/-ZWe-zRa3stE/XlTGFl7NksI/AAAAAAAAvmY/fR_RrfO6GAYdQSirnCC-bqvelI7LkUnYwCEwYBhgL/s1600/ACA5ABA1-3DDE-4042-8205-2572D5AFD0B5.JPG',
            actions=[
                MessageTemplateAction(
                    label='基隆市',
                    text='基隆市'
                ),
                 MessageTemplateAction(
                    label='台北市',
                    text='台北市'
                ),
                MessageTemplateAction(
                    label='桃園市',
                    text='桃園市'
                ),
                MessageTemplateAction(
                    label='新竹縣',
                    text='新竹縣'
                ),  

            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template2) 

