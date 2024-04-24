"""
Python3 中常见的数据类型有：
Number（数字）
String（字符串）
bool（布尔类型）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
此外还有一些高级的数据类型，如: 字节数组类型(bytes)。
"""

'''数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
在混合计算时，Python会把整型转换成为浮点数。
'''
print(20 / 3)
print(20 // 3)
print(20 % 3)  # 取余

# 用del 删除1个或者多个对象引用
'''
name1 = "liuyukun"
print(name1)
del name1
print(name1) 这里会报错  NameError: name 'name1' is not defined 未被定义
'''

# 关于bool类型
a = True
b = False
# 比较运算符
print(2 < 3)  # True
print(2 == 3)  # False
# 逻辑运算符
print(a and b)  # False 交集
print(a or b)  # True 并集
print(not a)  # False 非
# 类型转换
print(int(a))  # 1
print(float(b))  # 0.0
print(str(a))  # "True"

#
# List 列表
#

list1 = ['abcd', 786, 2.23, 'runoob', 70.2]  # 定义一个列表
tinylist = [123, 'runoob']

print(list1)  # 打印整个列表
print(list1[0])  # 打印列表的第一个元素
print(list1[1:3])  # 打印列表第二到第三个元素（不包含第三个元素） 左取右不取
print(list1[2:])  # 打印列表从第三个元素开始到末尾
print(tinylist * 2)  # 打印tinylist列表两次，在一个列表内
print(list1 + tinylist)  # 打印两个列表拼接在一起的结果,也是在一个列表内
# python列表内的元素是可变的
list1[0] = 'aaaa'
print(list1)
# python列表的切片也可以用步长
print(list1[0::2])
# 当步长为负数时，则是反向
print(list1[::-1])
list2 = ['Me', 'Love', 'Python']
print(list2[::-1])

#
# Tuple元组
#

# 元组和列表其实很像，不过元组是（），且里面的元素不能修改
tuple1 = ('I', 'love', 'Python')
tinyTuple1 = ('C++', 'Java')
print(tuple1)  # 输出完整元组
print(tuple1[0])  # 输出元组的第一个元素
print(tuple1[1:2])  # 输出从第二个元素开始到第三个元素
print(tuple1[2:])  # 输出从第三个元素开始的所有元素
print(tinyTuple1 * 2)  # 输出两次元组
print(tuple1 + tinyTuple1)  # 连接元组

# 修改元组内元素报错 TypeError: 'tuple' object does not support item assignment
# 虽然元组内元素不能改变，但是能包含可变化的元素，比如列表
tuple2 = ('I', 'love', 'Python', list1)
print(tuple2)
list1[0] = "abcd"
print(str(tuple2) + "\t改变了哦")
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
empty_tuple = ()
single_element_tuple = (20,)  # 必须要加一个逗号,当不加逗号时，会自动判断括号内的类型进行赋值
not_a_tuple = (20)
print(type(not_a_tuple))
print(empty_tuple)
print(single_element_tuple)

#
# Set 集合
#
# 集合的创建1.{}来创建 2.set()  set要多个单词或者什么的话，要多一个括号 即set(()) = {}
set1 = set("abc")
set2 = set(("apple","sumsung"))
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 'Zhihu'}
print(sites)  # 输出集合，重复的元素被自动去掉
print(set1)
print(set2)
# 元素是否在集合中
if 'Runoob1' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素 交叉部分


#
# 字典Dictionary 花括号 以key - value方式保存
#
dict1 = {}   #创建空字典而不是集合
dict1["language"] = "Python"
print(dict1)
dict1["language2"] = "C++"
print(dict1)
# 构造函数dict()
dict2 = dict([('language', 'Python'), ('language2', 'java')])
dict3 = dict(language = 'Python', language2= 'PHP')  # key 不要引号直接用就行
print(dict2)
print(dict3)

#
# bytes 类型  表示的是不可变的二进制序列
#

"""创建 byte类型对象的方法：
1.使用b前缀
2.使用byte()函数，第一个参数是要
"""
byte1 = b"hello"
print(byte1)