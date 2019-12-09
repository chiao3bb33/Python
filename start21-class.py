# Python 程式設計入門
# 類別的定義與使用
""" 
1.什麼是類別
2.封裝變數或函式
3.使用步驟
4.定義類別(建立類別)
5.使用類別
"""
""" .................什麼是類別................ """
# 什麼是類別
""" 
1.是Python語法的結構,用來封裝變數或函式
"""

""" .................封裝變數或函式................ """
# 封裝變數或函式
""" 
1.封裝的變數或函數統稱＿類別的屬性
"""

""" .................使用步驟................ """
# 使用步驟

# 定義 > 使用
""" 
1.要先定義(建立)類別
2.才能使用類別中封裝的屬性
"""

""" .................定義類別(建立類別)................ """
# 定義類別(建立類別)

# 基本語法
""" 
class 類別名稱: #首字不能使用數字 通常為大寫
    定義封裝的變數
    定義封裝的函式
"""
#程式範例 
""" 
class Test():  #定義test類別 
    x=3        #定義變數
    def say(): #定案函式
        print('hello') 
# x 與 say 就是 test 的屬性
"""

""" .................使用類別................ """
# 使用類別

# 基本語法
""" 
類別名稱 . 屬性名稱
"""
#程式範例 
""" 
class Test():  #定義test類別 
    x=3        #定義變數
    def say(): #定案函式
        print('hello') 
                                # x 與 say 就是 test 的屬性
#使用Test類別
Test.x+4     #取得屬性x的資料3  #result=7
Test.say()   #呼叫屬性say函式
"""
