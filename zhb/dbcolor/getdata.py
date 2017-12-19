import bs4
import urllib
import requests

currentPeriods=17147#当前期数
dburl="http://kaijiang.500.com/shtml/ssq/"+str(currentPeriods)+".shtml"#数据源

#获取网页的内容
req=requests.get(dburl)
req.encoding='utf-8'
htmlContent=req.text

soup=bs4.BeautifulSoup(htmlContent,'html.parser')#生成soup对象
htmlLiRed=soup.find_all('li',class_="ball_red")#红球
htmlLiBlue=soup.find_all('li',class_="ball_blue")#篮球

liBySort=[]

for li in htmlLiRed+htmlLiBlue:
    liBySort.append(li.string)
print(liBySort)



