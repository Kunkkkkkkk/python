# @Time:2024/3/26-14:58
# @Author:kun42910
# @File:_7.1my_module1.py
__all__ = ["test"]


def test(a, b):
    print(a + b)


def test2(a, b):
    print(a - b)


# main 的使用，即当测试用，在本文件里面调用的时候相当于 if true,在别的python文件里面调用模块的时候就不会调用这个测试
if __name__ == '__main__':
    test(1, 3)
