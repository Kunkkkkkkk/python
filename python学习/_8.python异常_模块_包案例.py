# @Time:2024/4/21-15:30
# @Author:kun42910
# @File:_8.python异常_模块_包案例.py

from my_utils import file_util
from my_utils import str_util

str1 = "liuyukun"
str1_rev = str_util.str_reverse(str1)
print(str1_rev)
str1_cut = str_util.substr(str1, 0, 2)
print(str1_cut)

file_address = "/Users/liuyukun/Downloads/dwqdaq.txt"
file_util.print_file_info(file_address)


