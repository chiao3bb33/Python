"""#if判斷式 基本語法"""
# TYPE A
# if 布林值:
# 若布林值為trun,執行命令
# else:
# 若布林值為False,執行命令

# TYPE B
# if 布林值一:
# 若布林值一為trun,執行命令
# elif 布林值二:
# 若布林值二為trun,執行命令
# else:
# 若布林值一和二為False,執行命令

# 程式範例
"""x=input('請輸入數字:') #基本輸入為字串型態
x=int(x) #轉換為整數型態
if x>200:
    print('大於200')
elif x>100:
    print('大於100, 小於200')
else:
    print('小於100')"""

# 判斷式
"""x=input('請輸入數字:') #取得字串形式的使用者輸入
x=int(x) #將字串型態轉換成數字型態#需要小數的話可以寫：x=float(x)
if x>200:
    print('大於100')
elif x>150:
    print('151~200')
else:
    print('小於100')"""

# 四則運算
n1 = int(input("輸入X:"))
op = input('請輸入運算符號:+,-,*,/:')
n2 = int(input("輸入Y:"))
if op == "+":
    print(n1+n2)
elif op == '-':
    print(n1-n2)
elif op == '*':
    print(n1*n2)
elif op == '/':
    print(n1/n2)
else:
    print('不支援運算')
