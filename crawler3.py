import urllib.request as req
url="https://vocus.cc/article/6285fba1fd89780001230aff"
#加header的目的是為了要讓爬蟲程式更像正常瀏覽者
#刷新網頁查看在f12 的 network 標籤裡面的網路連線的內容
#選擇你要看的網頁
#假如我這次要爬www.google.com 就選www.google.com欄位 並查看裡面的request header中的user-agent
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
    #"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
#print(data)
import bs4 
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div",class_="draft-block draft--p left")#
#print(root.title.string)
#print(titles)
for title in titles:
	if title.string != None:
		print(title.string)

		
		

