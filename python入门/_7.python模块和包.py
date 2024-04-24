# @Time:2024/3/26-14:49
# @Author:kun42910
# @File:_7.python模块和包.py

# 模块就是python文件
# 语法 from 模块名 import 功能名（函数名） as 别名
from time import sleep as sl

print("开始")
# time.sleep(5)
sl(5)
print("结束")

# 自定义模块
import my_module1

my_module1.test(1, 2)

# 当导入两个模块里的功能名相同时，会得到更下面的模块

# __all__变量和__main__变量,all就是from 模块 import * 时会导入的功能(其实就是函数)
# 包就是文件夹，模块文件+__init__.py
# import 包名.模块名

