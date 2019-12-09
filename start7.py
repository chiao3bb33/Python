# 迴圈進階控制
# break
# continue
# else
""" 迴圈搭配的指令
break 和 continue 均需在迴圈範圍內 """


# break 強制結束迴圈
"""
# 語法
(1)while 布林值:
    break
(2)for 變數名稱 in 列表或字串:
    break
           """
#eg#
"""
n=1
while n<5:
    if n==3:
        break
    n+=1
print('break ',n)
"""


# continue 強制繼續下一圈
"""
# 語法
(1)while 布林值:
    continue
(2)for 變數名稱 in 列表或字串:
    continue
"""
#eg#
"""
n=0      #T F T F T F
for x in [0,1,2,3,4,5]:
    if x%2==0:
        continue #Ture的話直接進入下一圈 False才進入n+=1
    n+=1
print('continue ',n)
"""

# 迴圈結構在最後面可以加入else的語法
""" 加入else語法
while 布林值:
    若布林值為ture,執行命令
    回到上方,做下一次的迴圈判斷
else:
    迴圈結束前,執行此區塊的命令
-------------------------------
for 變數名稱 in 列表或字串:
    逐一取出，逐一處理
    將列表中的項目或字串中的字元
else:
    迴圈結束前,執行此區塊的命令 """


# 程式碼驗證思考

""" n=1
while n<5:
    print('變數:',n)
    n+=1
else:
    print(n) #結束迴圈前,印出5 """


""" for c in 'hello':
    print('逐一',c)
else:
    print('結束',c) #結束迴圈前 印出O """


# break的簡易範例
""" n = 0
while n < 5:
    if n == 3:
        break
    print(n)  # 印出環圈中的n
    n += 1
print('最後的N', n)  # 印出迴圈結束後的N """

# continue的簡易範例
""" n = 0
for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    if x % 2 == 0:  # x是偶數
        continue
    print(x)
    n += 1
print("最後的N", n) """

# else的簡易範例
""" sum = 0
for n in range(11):
    sum += n
else:
    print(sum)  # 印出 0+1+2+...+10的結果 """

# 綜合範例:找出整數平方根
# 輸入9,得到3
# 輸入11, 得到[沒有]整數的平方根
n = input('輸入一個正整數')
n = int(n)
# 轉換輸入成數字
for i in range(n):  # i從0~n-1
    if i*i == n:
        print('整數平方根', i)
        break  # 用break 強制結束迴圈時 不會執行else區塊
else:
    print("沒有整數平方根")
