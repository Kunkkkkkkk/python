# @Time:2024/4/24-10:24
# @Author:kun42910
# @File:_15.带时间线的动态柱状图.py

# 实际上就是 bar 柱状图的嵌套，timeline柱状图的data 就是已经做好的 bar

from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType

# 构建每一个bar柱状图
bar1 = Bar()
data1 = ["中国","美国","日本"]
gdp1 = [10000,20000,15000]
bar1.add_xaxis(data1)
bar1.add_yaxis("GDP",gdp1)

bar2 = Bar()
data2 = ["中国","美国","日本"]
gdp2 = [15000,50000,30000]
bar2.add_xaxis(data2)
bar2.add_yaxis("GDP", gdp2)
# 构建时间柱状图
# 可以创建对象的时候可以设置主题
timeline = Timeline({"theme": ThemeType.LIGHT})   #更多主题去网上看资料
timeline.add(bar1,"2021")
timeline.add(bar2,"2022")
# 设置自动播放
timeline.add_schema(
    play_interval=1000,       # 设置自动播放间隔，单位毫秒， interval n.间隔
    is_timeline_show=True,   # 是否在播放的时候显示时间线
    is_auto_play=True,        # 是否自动开始播放  默认 False
    is_loop_play=False        # 是否循环播放 默认True

)
timeline.render("timeline入门.html")


