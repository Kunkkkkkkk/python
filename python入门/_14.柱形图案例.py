# @Time:2024/4/24-10:13
# @Author:kun42910
# @File:_14.柱状图案例.py

from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

data = ["中国","美国","日本"]
GDP = [20000,70000,50000]
bar = Bar()
bar.add_xaxis(data)
bar.add_yaxis("GDP",GDP,color="red",label_opts=LabelOpts(position="right"))   # 改变颜色,改变数值标签位置
bar.reversal_axis()  # 可以翻转x，y轴
bar.render("中美日gdp柱状图.html")
