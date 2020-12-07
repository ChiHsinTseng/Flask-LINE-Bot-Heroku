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
        buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
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
        line_bot_api.reply_message(event.reply_token, buttons_template)
    
    elif event.message.text == "錯誤回報":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "請點選以下連結：https://reurl.cc/14RmVW"))
    
    elif event.message.text == "最愛清單":
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='data:image/jpeg;base64,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',
                title='拉麵一號店',
                text='有夠好吃拉',
                actions=[
                    #PostbackTemplateAction(
                        #label='地址：台北市士林區',
                        #text='地址：台北市士林區',
                        #data='action=buy&itemid=1'
                    #),
                    MessageTemplateAction(
                        label='地址：台北市士林區',
                        text='地址：台北市士林區'
                    ),
                    URITemplateAction(
                        label='拉麵一號店心得文',
                        uri='https://bit.ly/2QmFNoJ'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='data:image/jpeg;base64,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',
                title='拉麵好吃二號店',
                text='也是有夠好吃拉',
                actions=[
                    #PostbackTemplateAction(
                        #label='postback2',
                        #text='postback text2',
                        #data='action=buy&itemid=2'
                    #),
                    MessageTemplateAction(
                        label='地址：台北市中山區',
                        text='地址：台北市中山區'
                    ),
                    URITemplateAction(
                        label='拉麵二號店心得文,
                        uri='https://bit.ly/3nEt4gv'
                    )
                ]
            )
        ]
    )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
