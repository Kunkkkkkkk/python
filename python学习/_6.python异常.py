# @Time:2024/3/26-14:33
# @Author:kun42910
# @File:_6.python异常.py

# 基本捕获语法
"""1.
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码


2.捕获指定异常
try:
    可能发生错误的代码
except Error as e:
    如果出现异常执行的代码

"""

try:
    x = 1 / 0
except ArithmeticError as e:
    print("除数不能为0")


"""
3.捕获多个异常
except (ArithmeticError,IoError) as e:
4.捕获所有异常 其实就是第一种基础语法或者 
except Exception as e
"""


"""
5.异常的else和finally语法
try:
    
except Exception as e:

else:
    如果没有异常会做的事
finally:
    有没有异常都会做的事 比如 f.close 等资源的释放

"""


# 异常会传递
