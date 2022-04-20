import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
#加header的目的是為了要讓爬蟲程式更像正常瀏覽者
#刷新網頁查看在f12 的 network 標籤裡面的網路連線的內容
#選擇你要看的網頁
#假如我這次要爬www.google.com 就選www.google.com欄位 並查看裡面的request header中的user-agent
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
print(data)
import bs4