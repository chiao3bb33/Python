# 定義函式
""" 函式內部的程式碼，若是沒有做函式呼叫，就不會執行 """
# 不含回傳值
""" # def multiply(n1, n2):
#     print(n1*n2)
# # 呼叫函式
# multiply(3, 4)
# multiply(10, 8) """


# 含回傳值
""" def multiply(n1, n2):
    print(n1*n2)
    return n1*n2
# 呼叫函式
value = multiply(3, 4)
print(value) """


# eg
# def multiply(n1, n2):
#     return n1*n2


# value = multiply(3, 4)+multiply(8, 8)-multiply(4, 2)
# print(value)

# ###程式的包裝###
#函式可用來做成式的包裝: 同樣的邏輯可以重複利用

def calculate(max):
    sum = 0
    max = input("輸入:")
    max = int(max)
    for n in range(1, max+1):
        sum += n
    print(sum)


calculate(max)
calculate(max)
calculate(max)
