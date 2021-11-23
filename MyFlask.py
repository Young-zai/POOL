import re
from typing import List, Mapping
from flask import Flask,render_template,request
import pandas as pd
#创建web应用程序
app = Flask(__name__, template_folder='templates')

@app.route("/")#装饰器（路由）
def show():
    data = pd.read_csv("不同类型电影票房平均值.csv")
    data = data.rename(columns={"电影类型":"name","累计票房":"value"})
  
  
    data = data.to_dict(orient="records")
    return render_template("show.html",data=data) #返回的数据（响应）
    
        
if __name__ == '__main__':  #程序入口
    app.run()


