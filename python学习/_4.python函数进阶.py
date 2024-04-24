# @Time:2024/3/25-08:17
# @Author:kun42910
# @File:_4.python函数进阶.py


"""
多个返回值，return用逗号隔开多个变量
"""


def my_func1():
    return 1, 2, "python"


def my_func2(name, age, gender):
    print(name, age, gender)


def my_func3(name, age, gender='male'):
    print(name, age, gender)


def my_func4(*args):
    print(args)


def my_func5(**kwargs):
    print(kwargs)


def my_func6(compute):
    r = compute(1, 2)
    print(f"结果是{r}")


"""
传参形式
1.位置参数
2.关键字参数：键 = 值
ps：当位置参数和关键字参数混用的时候，位置参数得放在最前面，不然会语法错误
3.缺省参数：就是有默认值,但是设置默认值必须放在最后不然会报错
4.不定长参数：不知道参数数量
4_1位置传递    '*'      得到的是元组 args
4_2关键字传递  '**'      得到的是键值对类型的字典  kwargs  kw是keyword
"""
x, y, z = my_func1()
my_func2(name="zhangsan", gender="male", age=10)  # 可以不按顺序
my_func2("lisi", 18, "female")
my_func3(name="zhangsan", age=10)
my_func4("zhangsan", "lisi", "wangwu")
my_func5(top1='k', top2='n', top3='m')

"""
函数本身可以把函数当参数传递，其实就是一个函数里面要调用另一个函数的时候就要传入那个函数
lambda 参数 : 函数体 

匿名函数 lambda 只能用一次，没有函数名,但是简单
"""
my_func6(lambda x, y: x + y)
