# @Time:2024/4/21-16:06
# @Author:kun42910
# @File:_10.pyecharts模块可视化.py

# 详细设置参数去官方文档 pyecharts.org

# 官网有一个 画廊  gallery.pyecharts.org


# 入门内容1.画一个折线图 2.学会全局配置项
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

line = Line()  # 得到折线图对象
line.add_xaxis(["软件1班", "软件2班", "软件3班", "软件4班"])  # x axis添加一个列表，就是横坐标
line.add_yaxis("班级人数", [20, 30, 15, 22])

# 常用的两个配置项 1、全局配置项  command + p  可以看很多配置项 2、系列配置项（后面学）

line.set_global_opts(title_opts=TitleOpts(title="统计人数", pos_left="center", pos_bottom="1%"),
                     legend_opts=LegendOpts(is_show=True),  # 这个legend 是图例组件
                     toolbox_opts=ToolboxOpts(is_show=True),  # 这个是工具箱  还有很多配置项不一一举例了
                     visualmap_opts=VisualMapOpts(is_show=True)
                     )

line.render()  # 生成图表  render 渲染
# 关于render的参数之后看，比如文件生成位子
