#這段是給mac電腦使用的
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
""" #抓取PTT電影版的網頁原始碼(HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/HatePolitics/index.html"
#建立一個request物件，附加Requset Headers的資訊
#仿照瀏覽器查詢樣態
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
#利用request物件去打開網址,不要帶入url到urlopen內
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)

#解析原始碼,取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
print(root.title.string) """

#抓取PTT電影版的網頁原始碼(HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/Lifeismoney/index2739.html"
#建立一個request物件，附加Requset Headers的資訊
#仿照瀏覽器查詢樣態
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
#利用request物件去打開網址,不要帶入url到urlopen內
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)

#解析原始碼,取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="title") #尋找class="title"的div標籤
#print(titles)
for title in titles:
    if title.a !=None: #如果標題包含a標籤(沒有被刪除)就會抓出來
        print(title.a.string)