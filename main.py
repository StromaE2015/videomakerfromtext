
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
from functions import replace_words_in_file, read_text_from_file


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

# استبدال الاعدادات القديمة بالجديدة
replace_words_in_file(newconfigfile, replacements)
# استيراد الاعدادات من الملف
text = read_text_from_file(newconfigfile)
# مراسلة chat gpt
 query_result = chatbot.chat(text)
# طباعة الرد من chat gpt
print(query_result) # or query_result.text or query_result["text"]







