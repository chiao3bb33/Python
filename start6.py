# while 迴圈
# 語法 while 布林值:
"""若布林值為true ,執行命令,回到上方,做下一次迴圈判斷"""
#EG#
""" n = 1
while n < 15:
    print('n變數:', n)
    n += 2
# ------------------------------
x = 3
while x < 200:
    print('X變數', x)
    x **= 3 """

# 程式碼驗證思考
"""n=1
while n<=5:
    print('變數:',n)
    # n+=1"""

# 等差級數的加法1+2+...+n
""" n = 1
x = input('輸入N:')
x = int(x)
sum = 0  # 紀錄累加的結果
while n <= x:
    sum += n  # sum=sum+n
    n += 1  # n=n+1
print("等差級數+N=", sum)"""


# for 迴圈
# 語法 for 變數名稱 in 列表或字串:
"""將列表中的項目或字串中的字元逐一取出，逐一處理"""
#EG#
""" for x in [4, 1, 2]:
    print('逐一取得列表中的資料：', x)

for x in 'hello':
    print('逐一取得字元中的資料：', x) """

# 使用range()  #製造連續數字的列表
"""#語法 for 變數名稱 in range(3):
#相當於
#for 變數名稱 in [0,1,2]:"""
# 語法 for 變數名稱 in range(3,6):
# 相當於
# for 變數名稱 in [3,4,5]:


# 程式碼驗證思考

""" for x in [3, 5, 1]:
    print(x)
for x in ['Hello', 'Life']:
    print(x)
for x in 'Hey':
    print(x) """

# range()用法
""" for x in range(6):
    print('typeA =', x)
for x in range(3, 6):
    print('typeB =', x) """

# 等差級數的加法1+...R+10
# 驗證過程均print
""" sum = 0
for x in range(1, 11):
    sum += x  # sum=sum+x
    print('驗證過程均print', sum)
# 僅結果
sum = 0
for x in range(1, 11):
    sum += x  # sum=sum+x
print('僅結果', sum) """
