

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




# Log in to huggingface and grant authorization to huggingchat
EMAIL = "kaboalby2015@gmail.com"
PASSWD = "@7Ayak0s"
cookie_path_dir = "./cookies/" # NOTE: trailing slash (/) is required to avoid errors
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
# Create your ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"


def replace_words_in_file(file_path, replacements, title):
    """
    استبدال كلمات متعددة في ملف نصي.

    :param file_path: مسار الملف النصي.
    :param replacements: قاموس يحتوي على الكلمات القديمة كالمفاتيح والكلمات الجديدة كالقيم.
    """

        # فتح الملف في وضع القراءة
        with open(oldconfigfile, 'r', encoding='utf-8') as file:
            content = file.read()

        # استبدال الكلمات القديمة بالكلمات الجديدة
        for old_word, new_word in replacements.items():
            content = content.replace(old_word, new_word)

        # فتح الملف في وضع الكتابة
        with open(newconfigfile, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"تم استبدال الكلمات في الملف '{file_path}'.")

    except FileNotFoundError:
        print(f"الملف '{file_path}' غير موجود.")


        print(f"حدث خطأ في فك تشفير الملف '{file_path}'.")



def read_text_from_file(file_path):
    """
    قراءة نص من ملف نصي.

    :param file_path: مسار الملف النصي.
    :return: النص الموجود في الملف.
    """

        # فتح الملف في وضع القراءة
        with open(file_path, 'r', encoding='utf-8') as file:
            # قراءة محتويات الملف
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"الملف '{file_path}' غير موجود.")
        return None

        print(f"حدث خطأ في فك تشفير الملف '{file_path}'.")
        return None


    oldconfigfile = "/content/videomakerfromtext/oldconfig.txt"
    newconfigfile = "/content/videomakerfromtext/newconfig.txt"
    replacements = {
        "title": title,
        "tobic": tobic,
        "time": VideoTime,
        "language": VideoLanguage
    }

    # كود الذي قد يسبب خطأً
    # على سبيل المثال:
    replace_words_in_file(oldconfigfile, replacements)
    text = read_text_from_file(file_path)
    query_result = chatbot.chat(text)
    print(query_result)





