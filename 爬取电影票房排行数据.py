from os import write
from selenium import webdriver        
from lxml import etree
from GetType import Type  #将获取电影类型这一操作封装到GetType模块中
import csv
if __name__ == '__main__':
    #使用哪个浏览器进行爬取则使用哪个浏览器的驱动
    Google = webdriver.Chrome(executable_path='./chromedriver.exe')  #实例化谷歌浏览器对象(参数传入谷歌浏览器的驱动程序)
    Google.get('https://ys.endata.cn/BoxOffice/Ranking')   

    got_type = Type()  #实例化所封装的对象
    
    M_type = got_type.Getting_movietype() #返回电影类型
    i = 0 #初始化判断指标
    final = M_type#将Getting_movietype()返回值实例化成列表对象
    new_movie_data = []
    
    page_text = Google.page_source

    tree = etree.HTML(page_text)
    tr_list = tree.xpath('//*[@id="app"]/section/main/div/div[1]/div/section/section/section/section/div/div[3]/table/tbody/tr')#获取每一个tr标签
    title = tree.xpath('//*[@id="app"]/section/main/div/div[1]/div/section/section/section/section/div[1]/div[2]/table/thead/tr/th//text()')#获取标题信息
    new_title = list(title)  #将标题信息实例化成列表对象,否则后面插入其他标题这一操作进行不了
    new_title.insert(2,'电影类型')  #在索引2处插入电影类型这一标题
   
    movie_data = []  #初始化一个列表，将解析到的电影信息存放到列表中以供编辑
    for tr in tr_list:
        message = tr.xpath('./td//text()') #数据
        movie_data.append(message)  #将解析到的电影信息存放到列表中
        #实现对应movie_data和final对应索引的元素进行处理
        if i < 50:  #页面数据有50行        
            a = list(movie_data[i])  #movie_data中每一个数据进行列表实例化，为之后对其添加电影类型做准备
            b = str(final[i])  #强制转化成字符串
            a.insert(2,b.split('/')[0])  
            i = i + 1
            new_movie_data.append(a)
    print(new_movie_data)  #输出最终想要的数据
            
    
            
    with open('电影排行.csv','a',encoding='utf-8-sig',newline='') as fp:  #encoding='utf-8-sig':避免写入csv文件乱码

        writer =  csv.writer(fp) 
        writer.writerow(new_title)  #标题写入excel表格
        writer.writerows(new_movie_data)  #数据写入excle表格
        
            

        
        

