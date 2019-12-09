# 儲存檔案
""" 
file=open('data.txt',mode='w',encoding='utf-8') #開啟
file.write('測試中文\n好棒棒 \nHello File\nSecond Line') #操作
file.close #關閉 
"""
""" 
with open('data.txt',mode='w',encoding='utf-8')as file:
    file.write('測試中文\n好棒棒') 
"""

# 讀取檔案
# 把檔案中的數字資料，一行一行的讀取出來並計算總合

""" with open('data.txt', mode='r', encoding='utf-8')as file:
    x=file.read()
print(x) 
"""

""" sum = 0
with open('data.txt', mode='r', encoding='utf-8')as file:
    for x in file:
        sum += int(x)  # 一行一行的讀取
print(sum)
 """
# 使用JSON格式讀取,複寫檔案
# 從檔案中讀取JSON資料,放入變數 x 裡面
import json
with open('config.json', mode='r')as file:
    x = json.load(file)
print(x)  # X 是一個字典資料
""" print('name:',x['name'])
print('version:',x['version']) """
x['name'] = 'New Name'  # 修改變數中的資料
#把最新的資料複寫回檔案中
with open('config.json', mode='w')as file:
    json.dump(x,file)