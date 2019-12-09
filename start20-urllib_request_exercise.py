# 網路連線
import urllib.request as req
# TYPE A
""" 
x="https://www.ntu.edu.tw"
with req.urlopen(x) as response:
    data=response.read().decode('utf-8') #.decode=解碼指定
    #取得台灣大學網站的原始碼(HTML,CSS,JS)
print(data) 
"""
# TYPE B 從網路上直接擷取資料 (讀取網路資料 另存為Ａ檔案資料)
import json
""" x = 'https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=f8ca3d5d-fc6f-4290-834d-9114cfbe7e33'
with req.urlopen(x) as response:
    y = json.load(response)  # 利用 json模組處理 json資料格式
# 將設計人名稱列表出來
clist = y['result']['results']  #轉換為列表 #邏輯來自觀察資料的程式語感result內有results的列表
with open('data.txt', 'w', encoding='utf-8') as file:
    for Designer in clist:
        file.write(Designer['構造種類']+"\n") """

#TYPE C (讀取Ａ檔案格式 另存為Ｂ檔案文字資料)
#已貼上檔案內容至新增的JSON檔案中 同步修正錯誤部分後 擷取部分資料
#資料來源:https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=11c9a165-b481-4c5f-b42c-5032cc59dc5e
""" with open('name.json', mode='r')as file:
    y = json.load(file)
clist = y['result']['results']  #轉換為列表 #邏輯來自觀察資料的程式語感result內有results的列表
with open('使用執照名冊.txt', 'w', encoding='utf-8') as file:
    for Designer in clist:
        file.write("設計人："+Designer['設計人']+"\n""承造人："+Designer['承造人']+"\n")
 """