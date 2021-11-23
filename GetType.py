#获取电影类型
import requests
from selenium import webdriver  
from lxml import etree
import concurrent.futures
class Type(object):

    def __init__(self) -> None:
        super().__init__()

    
    def Getting_movietype(self):
        url = 'https://ys.endata.cn/enlib-api/api/home/getrank_mainland.do'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'Referer': 'https://ys.endata.cn/BoxOffice/Ranking'
        }
        data = {
            'r': '0.4237929329022021',
            'top': '50',
            'type': '0'
        }
        response = requests.post(url=url,headers=headers,data=data)
        detail_data = response.json()
        movie_ID = []
        movie_type = []   #用于之后存放所解析到的电影类型
                
        for dic in detail_data['data']['table0']:
            movie_ID.append(dic['EnMovieID'])

        urls = []

        for ID in movie_ID:
            detail_movieurl = 'https://ys.endata.cn/Details/Movie?entId='+str(ID)
            
            urls.append(detail_movieurl)

        def craw(url):    #阻塞操作，封装到一个函数中放到线程池运行

            Google = webdriver.Chrome(executable_path='./chromedriver.exe')  #实例化谷歌浏览器对象(参数传入谷歌浏览器的驱动程序)
            Google.get(url) 
            type_text = Google.page_source
            tree = etree.HTML(type_text)
            typer = tree.xpath('//*[@id="app"]/section/main/div/div[1]/div/section/section[1]/div[1]/div/p[4]/span/text()')
            
            return typer

        

        with concurrent.futures.ThreadPoolExecutor() as pool:   #创建线程池，实现线程重用，减少新建/终止线程的开销
            htmls = pool.map(craw,urls)    #页面原码数据
            htmls = list(zip(urls,htmls))
            for url,t in htmls:
                movie_type.append(t)
            
        return movie_type
        


