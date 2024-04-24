# @Time:2024/4/23-09:51
# @Author:kun42910
# @File:_12.地理图案例.py

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map1 = Map()
# 列表嵌套元组，（地址名，值）

data = [("北京市", 500),
        ("上海市", 100000),
        ("广东省", 200)]
# maptype 可以在pyecharts下面的datasets里的map_filename.json里面查找所需
map1.add("地图", data, "china")
map1.set_global_opts(
    visualmap_opts=VisualMapOpts(is_show=True,
                                 is_piecewise=True,
                                 pieces=[{"min": 0, "max": 100, "label": "0~100人", "color": "#CCFFFF"},
                                         {"min": 101, "max": 1000, "label": "101~1000人","color":"#FF9966"},
                                         {"min": 1001, "max":10000, "label": "1001~10000","color":"CC3333"},
                                         {"min":10000, "label": "10000以上","color":"#990033"}
                                 ]
                                 )
    # is_piecewise是开启手动校准范围,piece是列表类型，里面是字典类型

)

map1.render("中国地图.html")
