from hugchat import hugchat
from hugchat.login import Login
import re
import os

# تعريف المتغيرات
title = "مخدر الحشيش"  # @param {type:"string"}
tobic = "مخدر الحشيش"  # @param {type:"string"}
VideoTime = "5"  # @param {type:"string"}
VideoLanguage = "عربي"  # @param {type:"string"}

# Log in to huggingface and grant authorization to huggingchat
EMAIL = "kaboalby2015@gmail.com"
PASSWD = "@7Ayak0s"
cookie_path_dir = "./cookies/"  # مسار مجلد الكوكيز
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
# Create your ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"


def replace_words_in_file(file_path, replacements, title):
    """
    استبدال كلمات متعددة في ملف نصي.

    :param file_path: مسار الملف النصي.
    :param replacements: قاموس يحتوي على الكلمات القديمة كمفاتيح والكلمات الجديدة كقيم.
    :param title: العنوان الذي يتم استخدامه في الاستبدال.
    """
    try:
        # فتح الملف في وضع القراءة
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # استبدال الكلمات القديمة بالكلمات الجديدة
        for old_word, new_word in replacements.items():
            content = content.replace(old_word, new_word)

        # فتح الملف في وضع الكتابة
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"تم استبدال الكلمات في الملف '{file_path}'.")
    except FileNotFoundError:
        print(f"الملف '{file_path}' غير موجود.")
    except Exception as e:
        print(f"حدث خطأ في فك تشفير الملف '{file_path}': {e}")

def read_text_from_file(file_path):
    """
    قراءة نص من ملف نصي.

    :param file_path: مسار الملف النصي.
    :return: النص الموجود في الملف.
    """
    try:
        # فتح الملف في وضع القراءة
        with open(file_path, 'r', encoding='utf-8') as file:
            # قراءة محتويات الملف
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"الملف '{file_path}' غير موجود.")
        return None
    except Exception as e:
        print(f"حدث خطأ في فك تشفير الملف '{file_path}': {e}")
        return None

def wait_for_response(chatbot, text):
    """
    انتظر حتى يتم الرد من الروبوت.

    :param chatbot: كائن الشات بوت.
    :param text: النص الذي يتم إرساله إلى الشات بوت.
    :return: الرد من الشات بوت.
    """
    response = chatbot.chat(text)
    return response

def extract_lines_starting_with_prefix(text, prefix):
    """
    استخراج الأسطر التي تبدأ ببادئة محددة من النص.

    :param text: النص الذي يحتوي على الأسطر.
    :param prefix: البادئة التي يجب أن تبدأ الأسطر بها.
    :return: قائمة بالأسطر التي تبدأ بالبادئة المحددة.
    """
    lines = re.findall(rf'{prefix}\d+\s*=\s*(.*)', text)
    return lines

def write_lines_to_file(lines, file_path):
    """
    كتابة الأسطر إلى ملف نصي.

    :param lines: قائمة بالأسطر التي يجب كتابتها.
    :param file_path: مسار الملف النصي.
    """
    with open(file_path, "w") as file:
        for line in lines:
            file.write(line.strip() + "\n")
    print(f"تم إنشاء ملف {file_path} بنجاح.")

# تحديد المسار الذي يتم فيه إنشاء الملف
current_directory = os.getcwd()
file_path_image = os.path.join(current_directory, "image_lines.txt")
file_path_video = os.path.join(current_directory, "video_lines.txt")
file_path_text = os.path.join(current_directory, "text_lines.txt")

# قراءة النص من الملف
oldconfigfile = os.path.join(current_directory, "oldconfig.txt")
newconfigfile = os.path.join(current_directory, "newconfig.txt")

replacements = {
    "title": title,
    "tobic": tobic,
    "time": VideoTime,
    "language": VideoLanguage
}

# استبدال الكلمات في الملف
replace_words_in_file(newconfigfile, replacements, title)

# قراءة النص من الملف
text = read_text_from_file(newconfigfile)

if text:
    # انتظار الرد من الشات بوت
    response = wait_for_response(chatbot, text)
    print(response)
    
    # استخراج الأسطر التي تبدأ بـ "image" وكتابتها في ملف نصي
    image_lines = extract_lines_starting_with_prefix(response.text, "image")
    write_lines_to_file(image_lines, file_path_image)
    
    # استخراج الأسطر التي تبدأ بـ "video" وكتابتها في ملف نصي
    video_lines = extract_lines_starting_with_prefix(response.text, "video")
    write_lines_to_file(video_lines, file_path_video)
    
    # استخراج الأسطر التي تبدأ بـ "text" وكتابتها في ملف نصي
    text_lines = extract_lines_starting_with_prefix(response.text, "text")
    write_lines_to_file(text_lines, file_path_text)
else:
    print("لا يمكن قراءة النص من الملف.")
