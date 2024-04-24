# @Time:2024/4/24-09:47
# @Author:kun42910
# @File:_13.全国各省疫情确诊情况地理图案例.py

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
import json

f = open("/Users/liuyukun/资料/python黑马/资料/第1-12章资料/资料/可视化案例数据/地图数据/疫情.txt", 'r',
         encoding="utf-8")

# 获取到文件信息转为python类型
content = f.read()
f.close()
content = json.loads(content)
list1 = content["areaTree"][0]["children"]
data = []
# 获取列表含元组的形式
# 这里是重点，假如后面没有这个 省或者市的话，地图不会显示
for i in list1:
    data.append((i["name"]+"省", i["total"]["confirm"]))

map1 = Map()
map1.add("确诊人数", data, maptype="china")
map1.set_global_opts(visualmap_opts=VisualMapOpts(is_show=True,
                                                  is_piecewise=True,
                                                  pieces=[
                                                      {"min": 1, "max": 100, "label": "1~100人", "color": "#0000CD"},
                                                      {"min": 101, "max": 400, "label": "1~400人", "color": "#7FFF00"},
                                                      {"min": 401, "max": 1000, "label": "401~1000人",
                                                       "color": "#7CFC00"},
                                                      {"min": 1001, "max": 3000, "label": "1001~3000人",
                                                       "color": "#FFFF00"},
                                                      {"min": 3001, "max": 5000, "label": "3001~5000人",
                                                       "color": "#8B4513"},
                                                      {"min": 5000, "max": 10000, "label": "5001~10000人",
                                                       "color": "#FFB6C1"},
                                                      {"min": 10000, "max":30000, "label": "10000~30000人",
                                                       "color":"#C71585"},
                                                      {"min": 30000,"label":"3w人以上","color":"#C6E2FF"}
                                                      ]))
map1.render("各省疫情确诊情况地理图.html")