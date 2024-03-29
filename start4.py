"""#集合# 一群資料 沒有順序"""
# 使用in和not in運算符號
# 兩個集合 使用交集及聯集運算 使用$和|運算符合
# 兩個集合 使用差集及反交集運算 使用-和^運算符合
# 字串拆解為集合 set(字串)

# 集合的運算
"""s1={3,4,5}
print(3 in s1)
print(10 not in s1)
print(10 in s1)

s1={3,4,5}
s2={4,5,6,7}"""
# 交集:取兩個集合中,相同的資料
"""s3=s1&s2 
print(s3)"""
# 聯集:取兩個集合中的所有的資料, 但不重複取
"""s3=s1|s2 
print(s3)"""
# 差集:從S1中,減去和S2重疊的部分
"""s3=s1-s2 
print(s3)"""
# 反交集:取兩個集合中，不重疊的部分
"""s3=s1^s2 
print(s3)"""
s = set('hello')  # 把字串拆解成集合
print(s)
# 建立集合 #set(字串)
"""s=set('hello') #把字串拆解成集合
print(s)
print('h'in s)
print('a'in s)"""


"""#字典# 鑑值對(key-value pair)"""
# Key 對應 Value
#字典[key] = Value
# 使用in和not in運算符號
# 刪除鑑值對 使用del運算關鍵字
# 以列表的資料為基礎來建立字典

# 字典的運算:key-value配對
"""dic={'apple':'蘋果','bug':'蟲蟲'}
print(dic['apple'])
dic['apple']='小蘋果'
print(dic['apple'])
print('apple'in dic) #判斷Key是否存在
print('app'in dic)"""

# 刪除字典中的key-value pair
"""dic={'apple':'蘋果','bug':'蟲蟲'}
print(dic)
del dic['apple'] 
print(dic)"""

# 列表的資料當基礎產生字典
"""#dic={x:x*2 for x in 列表}
dic={x:x*2 for x in [3,4,5]} #從列表的資料當基礎產生字典
print(dic)"""
