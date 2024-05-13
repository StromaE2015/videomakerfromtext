
!pip install hugchat pillow opencv-python moviepy pyttsx3 pydub tk

from hugchat import hugchat
from hugchat.login import Login
import re
import cv2
import numpy as np
from PIL import Image
from moviepy.editor import *
from pyttsx3 import init
from pydub import AudioSegment
from pydub.playback import play
import sys


# @title Default title text
title = "اشباح تم التقاطها بواسطة كاميرات cctv" # @param {type:"string"}
tobic = "اشباح تم التقاطها بواسطة كاميرات cctv" # @param {type:"string"}
VideoTime = "5" # @param {type:"string"}
VideoLanguage = "عربي" # @param {type:"string"}

# Log in to huggingface and grant authorization to huggingchat
EMAIL = "kaboalby2015@gmail.com"
PASSWD = "@7Ayak0s"
cookie_path_dir = "./cookies/" # NOTE: trailing slash (/) is required to avoid errors
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

# Create your ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"


replace_words_in_file(newconfigfile, replacements)



# مثال على الاستخدام
file_path = newconfigfile
text = read_text_from_file(file_path)
if text:
 query_result = chatbot.chat(text)
print(query_result) # or query_result.text or query_result["text"]







