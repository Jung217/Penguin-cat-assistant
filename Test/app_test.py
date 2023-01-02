from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from io import StringIO
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import requests
import re
import os
import random
import configparser
from PIL import Image
import pyimgur

def glucose_graph(client_id, imgpath):
	im = pyimgur.Imgur(client_id)
	upload_image = im.upload_image(imgpath, title="Uploaded with PyImgur")
	return upload_image.link


#SendImage = line_bot_api.get_message_content(event.message.id)

local_save = 'Penguin-cat-assistant\pic\me.png'
#with open(local_save, 'wb') as fd:
#    for chenk in SendImage.iter_content():
#        fd.write(chenk)

img_url = glucose_graph("d8f43d95eef9f03", local_save)
print(img_url)
#line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
