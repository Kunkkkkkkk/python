# @Time:2024/4/21-17:10
# @Author:kun42910
# @File:_11.折线图案例.py

# json着色懒人工具 ab173.com
import json
from pyecharts.charts import Line
from pyecharts.options import ToolboxOpts, TitleOpts, VisualMapOpts, LabelOpts

# 打开文件进行读取
fus =open("/Users/liuyukun/上课辅助/美国.txt", "r", encoding="utf-8")
fjp =open("/Users/liuyukun/上课辅助/日本.txt", "r", encoding="utf-8")
fin =open("/Users/liuyukun/上课辅助/印度.txt", "r", encoding="utf-8")
content1 = fus.read()
content2 = fjp.read()
content3 = fin.read()
# 处理数据，这里说白了直接在文件里手动删就行了

# 把数据转为python格式(字典格式)
content1 = json.loads(content1)
content2 = json.loads(content2)
content3 = json.loads(content3)
# 取到314之前的日期数据，作为x轴
us_list_updateDate = content1["data"][0]["trend"]["updateDate"][:314]
# 取到314之前的日期的确诊数据，作为y轴
us_list_diagnosed = content1["data"][0]["trend"]["list"][0]["data"][:314]
jp_list_diagnosed = content2["data"][0]["trend"]["list"][0]["data"][:314]
in_list_diagnosed = content3["data"][0]["trend"]["list"][0]["data"][:314]
# 必须先创建对象
line = Line()
# 设置工具箱
line.set_global_opts(
    title_opts=TitleOpts(title="美，日，印疫情状况",pos_left='center',pos_bottom='0'),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
line.add_xaxis(us_list_updateDate)
line.add_yaxis("美国确诊人数", us_list_diagnosed, label_opts=(LabelOpts(is_show=False)))
line.add_yaxis("日本确诊人数", jp_list_diagnosed, label_opts=(LabelOpts(is_show=False)))
line.add_yaxis("印度确诊人数", in_list_diagnosed, label_opts=(LabelOpts(is_show=False)))
line.render("疫情.html")
fus.close()
fjp.close()
fin.close()
