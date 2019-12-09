# Python 程式設計入門
# 讀取,儲存文字檔案
""" 
1.檔案操作流程
2.開啟檔案(開啟模式)
3.開啟模式
4.讀取檔案
5.寫入檔案 (儲存檔案)
6.關閉檔案
7.Python 提供最佳實務語法
"""
""" .................檔案操作流程................ """
# 檔案操作流程
""" 
開啟檔案 > 讀取或寫入 > 關閉檔案
"""

""" .................開啟檔案................ """
# 開啟檔案

# 基本語法
""" 
1.檔案物件=open(檔案路徑, mode=開啟模式)
2.檔案物件=open(檔案路徑, mode=開啟模式,encoding='utf-8')

"""
""" .................開啟模式................ """
# 開啟模式

""" 
讀取模式 - r
寫入模式 - w
讀寫模式 - r+
"""

""" .................讀取檔案................ """
# 讀取檔案

# 基本語法
""" 
1.讀取全部文字
檔案物件 . read()

2.一次讀取一行
for 變數 in 檔案物件 :
    從檔案依序讀取每行文字到變數中

3.讀取 JSON格式  #交換資料 或 儲存設定檔
import json #載入模組
讀取到的資料=json.load(檔案物件)

"""

""" .................寫入檔案 (儲存檔案)................ """
# 寫入檔案 (儲存檔案)

# 基本語法
""" 
1.寫入文字 
檔案物件 . write(字串) 

2.寫入換行符號
檔案物件 . write("字串\n") 

3.寫入 JSON格式  
import json #載入模組
json.dump(要寫入的資料, 檔案物件)

"""

""" .................關閉檔案................ """
# 關閉檔案

# 基本語法
""" 
檔案物件 . close() 
"""

""" .................Python 提供最佳實務語法................ """
# 最佳實務

# 基本語法
""" 
with open(檔案路徑, mode=開啟模式)as檔案物件:
    讀取或寫入檔案的格式

#以上區塊會自動,安全的關閉檔案
#採用此語法就不用設定close 並且安全的關閉

"""
