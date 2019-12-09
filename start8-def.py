# ###函式###
""" 函式=程式區塊
函式:程式碼包裝在一個區塊中,方便隨時呼叫使用 """

# 程式中使用"函式" 有兩個步驟
# 1.定義 > 2.呼叫
""" 要先定義(建立)函式,然後才能呼叫(使用)函式 """

# ###定義函式###
""" 基本語法 """
""" 
def 函式名稱 (參數_名稱) :
    函式內部的程式碼 """
# 參數可以讓函式有彈性


# 程式範例
""" 定義一個印出Hello的函式 """
# def sayHello():
#     print('Hello')
""" 定義可以印出任何訊息的函式 """
# def say(msg):
#     print(msg)
""" 定義一個可以做加法的函式 """
# def add(n1, n2):
#     result = n1+n2
#     print(result)


# ###呼叫函式###
""" 基本語法 """
""" 函式名稱 (參數_資料)"""
# 參數可以讓函式有彈性

# 程式範例
""" 定義一個印出Hello的函式 """
# def sayHello():
#     print('Hello')
""" 呼叫上方定義的函數 """
# sayHello()

""" ------------------------------ """

""" 定義可以印出任何訊息的函式 """
# def say(msg):
#     print(msg)
""" 呼叫上方定義的函數 """
# say('Hello Function')
# say('Hello python')

""" ------------------------------ """

""" 定義一個可以做加法的函式 """
# def add(n1, n2):
#     result = n1+n2
#     print(result)
""" 呼叫上方定義的函數 """
# add(3,4)
# add(7,8)

""" ------------------------------ """

""" ***函式流程非常重要*** """
""" Check語法→正確 Check流程:
1.定義函式(參數名稱)
2.呼叫函式(參數資料)
3.執行"呼叫"→程式跳到函式內的程式碼→執行完後，跳回到"呼叫"→繼續往下run coding """


# ###回傳值###
""" 基本語法 """
""" 
TYPE A:
def 函式名稱 (參數_名稱) :
    函式內部的程式碼
    return    #結束函數,回傳None 
    
TYPE B:
def 函式名稱 (參數_名稱) :
    函式內部的程式碼
    return 資料    #結束函數,回傳「資料」    
*資料: 數字,字串,布林值,物件...etc
"""

# 程式範例

# TYPE A
""" 函式回傳None """
# def say(msg):
#     print(msg)
#     return
""" 呼叫函式,取得回傳值 """
# value=say('Hello function')
# print(value) #印出None

# TYPE B
""" 函式回傳字串Hello """
# def add(n1,n2):
#     result = n1+n2
#     return"Hello"
""" 呼叫函式,取得回傳值 """
# value=add(3,4)
# print(value) #印出Hello

# TYPE C
""" 函式回傳n1+n2的結果 """
# def add(n1,n2):
#     result = n1+n2
#     return result
""" 呼叫函式,取得回傳值 """
# value=add(3,4)
# print(value) #印出7
