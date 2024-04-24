# @Time:2024/4/21-15:55
# @Author:kun42910
# @File:_9.python列表和字典与json格式的转换.py

import json

data = [{"name": "John", "age": 18}, {"name": "鲲", "age":20}]
# 把python数据转换成json数据
data1 = json.dumps(data)
print(data1)  # 此时会发现 鲲 字打印不出来，因为中文编码的问题，所以这里要再加一个参数
data1 = json.dumps(data,ensure_ascii=False)
print(data1)
# 把json数据转换成python数据
data2 = json.loads(data1)
print(type(data2))




