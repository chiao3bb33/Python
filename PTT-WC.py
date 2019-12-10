
import urllib.request as req
def getData(url):
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="title")

    for title in titles:
        if title.a !=None:
            con = title.a.string
            print(con)
            # with open("PTT3.txt", mode="a", encoding="utf-8") as file:
            #     file.write(con+'\n')


    nextLink=root.find("a",string="‹ 上頁")

    return nextLink["href"]



pageURL = "https://www.ptt.cc/bbs/creditcard/index.html"
count=0
while count<=10:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
