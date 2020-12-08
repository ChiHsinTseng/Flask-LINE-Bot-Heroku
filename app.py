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
        flex_message = FlexSendMessage(
        alt_text='hello',
        contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://media.timeout.com/images/105665255/630/472/image.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "你在哪裡？",
        "weight": "bold",
        "size": "xl",
        "contents": []
      },
      {
        "type": "text",
        "text": "請選擇你在台灣的哪裡 ",
        "size": "xs",
        "color": "#888888"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "北部",
              "text": "北部"
            },
            "style": "secondary",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "中部",
              "text": "中部"
            },
            "style": "secondary",
            "margin": "xxl",
            "height": "sm"
          }
        ],
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "南部",
              "text": "南部"
            },
            "style": "secondary",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "東部",
              "text": "東部"
            },
            "style": "secondary",
            "margin": "xxl",
            "height": "sm"
          }
        ],
        "margin": "md"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "我要開定位",
          "text": "我要開定位"
        },
        "style": "secondary",
        "height": "sm",
        "margin": "none",
        "position": "relative",
        "color": "#D9AE94"
      }
    ],
    "spacing": "sm",
    "margin": "none"
  }
}
        )

        line_bot_api.reply_message(event.reply_token,flex_message)



    elif event.message.text == "錯誤回報":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "請點選以下連結：https://reurl.cc/14RmVW"))

        
        
    elif event.message.text == "北部":       
        flex_message1 = FlexSendMessage(
        alt_text='北部的縣市',
        contents= {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "你在哪個縣市？",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "請幫助我選擇縣市讓你更快得到推薦喔！",
            "size": "xs",
            "color": "#888888"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "台北市",
              "text": "台北市"
            },
            "style": "secondary",
            "height": "sm"
          }
        ],
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "基隆市",
              "text": "基隆市"
            },
            "style": "secondary",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "新北市",
              "text": "新北市"
            },
            "style": "secondary",
            "height": "sm",
            "margin": "xxl"
          }
        ],
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "桃園市",
              "text": "桃園市"
            },
            "style": "secondary",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "新竹市",
              "text": "新竹市"
            },
            "height": "sm",
            "style": "secondary",
            "margin": "xxl"
          }
        ],
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "新竹縣",
              "text": "新竹縣"
            },
            "style": "secondary",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "苗栗縣",
              "text": "苗栗縣"
            },
            "style": "secondary",
            "height": "sm",
            "margin": "xxl"
          }
        ],
        "margin": "md"
      }
    ]
  }
}
        )
        
        line_bot_api.reply_message(event.reply_token,flex_message1) 
