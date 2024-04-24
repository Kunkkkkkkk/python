# @Time:2024/4/21-15:23
# @Author:kun42910
# @File:file_util.py
def print_file_info(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            text = f.read()
            print("文件内容为" + text)
    except Exception as e:
        print(e)
    finally:
        if f is not None:
            f.close()


def append_to_file(file_name, content):
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(content)
        f.close()
    print("追加写入完毕")
