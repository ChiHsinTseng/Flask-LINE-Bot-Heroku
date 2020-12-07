import os
from datetime import datetime

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

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
 
                if event.message.text == "拉麵推薦":
 
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='Menu',
                                text='請選擇地區',
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
                                    )
                                    MessageTemplateAction(
                                        label='東部',
                                        text='東部'
                                    )
                                ]
                            )
                        )
                    )

        
             else:
                    food = IFoodie(event.message.text)
 
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TextSendMessage(text=food.scrape())
                    )
 
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
