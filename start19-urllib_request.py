# Python 程式設計入門
# 網路連線,公開資料串接
""" 
1.學習 urllib.request 模組(內建模組)
2.亂數模組
3.讀取檔案
4.寫入檔案 (儲存檔案)
5.關閉檔案
6.Python 提供最佳實務語法
"""
""" .................內建模組................ """
# urllib.request 模組  ＃抓取公開資料
""" 
學習 urllib.request 模組
"""

""" .................網路連線................ """
# 亂數模組

# 載入模組
""" 
import urllib.request as request
"""
# 操作模組

# TYPE A 下載特定網址資料
""" 
1.with request.urlopen(網址)as response: #response="物件" 固定指令
    data=response.read()
print(data)
"""

""" .................公開資料................ """
#適合的資料來源 (北市政府的公開資料)
#確認資料的格式：JSON, CSV,或其他格式
#解讀JSON格式 (利用內建的JSON模組)