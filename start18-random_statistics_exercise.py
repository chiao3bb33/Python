""" 隨機模組 """
#載入模組
import random
#隨機選取
""" x=random.choice([1,5,6,7,8,19])
print(x)
x=random.sample([1,5,6,7,8,19],3)
print(x) """
#隨機調換順序
""" x=[1,5,6,37,344,23,345]
random.shuffle(x)
print(x) """
#隨機取得亂數
""" x=random.random() #0.0~1.0 之間的隨機亂數
print(x)
print('-------------------')
x=random.uniform(50, 100) #A~Z之間的隨機亂數
print(x) """
#取得常態分配亂數 （平均數100,標準差10 得到的資料多數在90~110之間）
""" x=random.normalvariate(100,10)
print(x)
print('---------------------')
x=random.normalvariate(1000,200)
print(x)
x=random.normalvariate(0,5)#平均數0, 標準差5,得到的資料多數在-5~5之間
print(x) """

""" 統計模組 """
#載入模組
import statistics as stat
#平均數
""" x=stat.mean([1,4,5,6,7])
print(x)
print('------------------')
x=stat.mean([1,4,5,6,7,1000])  #極端狀況出現
print(x) """
#中位數 (較不被極端的狀況影響)
""" x=stat.median([1,4,5,6,7,1000])
print(x) """
#標準差 (資料散佈的狀況)(資料之間的差距是否很大？) #常態分配
x=stat.stdev([1,2,3,4,5,6,7,8,10])
print(x)
print('-----------------------')
x=stat.stdev([1,2,3,4,5,6,7,8,1000])
print(x)