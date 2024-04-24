"""
内容：
标识符
python保留字
注释
行与缩进
多行语句
数字(Number)类型
字符串(String)
空行
输入
同一行显示多条语句
print
import

"""
import keyword

var = keyword.kwlist
print(var)  # python里的保留字

'''注释
多行注释
也可以用
'''
"""
单双引号都行
"""

# 行与缩进 indentation
if True:
    print("this is true")
else:
    print("this is false")

# 多行语句
a, b, c = 2, 3, 4
name1 = a + \
        b + \
        c  # 用“\”隔开
print(name1)

# Number类型
# int （在python3里没有Long）
# bool  True and False
# float 1.23,1+E 当字符串内容为浮点型时要转化成整形时不能直接用int（）的强转，得先用float的强转
number111 = "21.231"
print(int(float(number111)))

# complex 复数 例如1+2j，可以用 a + bj，或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是「浮点型」。


# String类型
# 在python中，单引号和双引号的作用完全相同
# '''和"""可以指定一个多行的字符串，例如
name2 = '''超级无敌
暴龙战士
鲲
'''
# 转义符 \ ,但是实用r可以使转义符号失效
print(r"可以输出 \n")  # 这里的r的意思是raw，即原始的输出
# 字符串可以用 + 号来链接，用 * 号来重复
print(name2 * 2)
print(name2 + str(name1))
# python中的字符串不能改变，重复赋值不算，比如
'''name3 = "datada"
name3[0] = 'A'
此时就会报错 ： TypeError: 'str' object does not support item assignment
'''
# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长] ,左包右不包
String429 = "1234567890"
print(String429)
print(String429[0:-1])  # 输出从1到9
print(String429[0:9:2])  # 相邻的数字差为2
print(String429 * 2)

# 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

# 用户输入
'''
input123 = int(input("Enter a number: "))
print(input123)
'''

# 使用 : 可以在一行内显示多行代码

# print的使用，默认换行输出，如要不换行输出则在末尾加上end= ""
print("这是第一行", end=',')
print("这不是第二行", end=' ')

# 关于import和form..import..
# import是导入整个模块，而form..i 可以是从一个模块里导入一部分东西
'''
例如将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''
