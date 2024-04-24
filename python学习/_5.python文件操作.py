# @Time:2024/3/25-08:50
# @Author:kun42910
# @File:_5.python文件操作.py

"""
open(name,mode,encoding)
当不存在这个文件会自动创建

mode: r只读 ,w写入，a追加

文件对象.read(number) number是字节长度，没有就全读取
当先读了一部分，下一次读就会从这个指针开始
f.readLines()  逐行读取封装到列表里

用with open就可以不用手动close
"""
# f =open("/Users/liuyukun/资料/ceshi.txt",'r',encoding="UTF-8")
with open("/Users/liuyukun/资料/ceshi.txt", 'r', encoding="UTF-8") as f:
    print(f.read(3))
    print(f.read(2))

'''
for循环逐行读取文件'''

# 案例：计数python出现的次数
with open("/Users/liuyukun/资料/ceshi.txt", 'r', encoding="UTF-8") as f:
    text = f.read()
    print(f"python出现次数：{text.count('python')}")
# 如果用逐行的化，剔除'\n' str.strip()  去除首尾的空格和换行符


# 写入操作里的close内置了flush
# 文件存在的时候， w模式会把内容全部清空

# 案例备份
with open("/Users/liuyukun/资料/ceshi.txt", 'r', encoding="UTF-8") as fr:
    with open("/Users/liuyukun/资料/ceshi_copy.txt", 'w', encoding="UTF-8") as fw:
        texts = fr.readlines()
        for text in texts:
            text = text.strip()
            if "正式" in text:
                fw.write(text)

        print("已经按要求备份")
