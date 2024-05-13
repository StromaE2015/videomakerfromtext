def replace_words_in_file(file_path, replacements):
    """
    استبدال كلمات متعددة في ملف نصي.

    :param file_path: مسار الملف النصي.
    :param replacements: قاموس يحتوي على الكلمات القديمة كالمفاتيح والكلمات الجديدة كالقيم.
    """
    try:
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

    except UnicodeDecodeError:
        print(f"حدث خطأ في فك تشفير الملف '{file_path}'.")

# مثال على الاستخدام
oldconfigfile = "/content/text.txt"
newconfigfile = "/content/text2.txt"
replacements = {
    "title": title,
    "tobic": tobic,
    "time": VideoTime,
    "language": VideoLanguage
}

