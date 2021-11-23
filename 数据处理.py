import pandas as pd
data = pd.read_csv("电影排行.csv")

#取电影类型和类机票房这两组数据，对其进行分析
data = data.loc[:,['电影类型','累计票房']]  

#以电影类型为分组对累计票房求平均值,将结果保留两位小数
data = data.groupby(['电影类型']).mean().round(2)  

#将结果写入新的csv中，用作之后的可视化分析
data.to_csv("不同类型电影票房平均值1.csv",encoding='utf-8-sig')
print(data)