import urllib.request as req
url="https://www.dcard.tw/f"
#加header的目的是為了要讓爬蟲程式更像正常瀏覽者
#刷新網頁查看在f12 的 network 標籤裡面的網路連線的內容
#選擇你要看的網頁
#假如我這次要爬www.google.com 就選www.google.com欄位 並查看裡面的request header中的user-agent
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
#print(data)
import bs4 
import re
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("h2",re.compile('sc'))#尋找class="title"的div標籤
#print(root.title.string)
#print(titles)
for title in titles:
	#if title.a != None:
	print(title.a.span.string)
		

