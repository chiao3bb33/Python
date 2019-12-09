""" .................預設資料................ """
# 參數的預設資料

""" def power(base,exp=0):
    print(base**exp)

power(3,2)
power(4) """

""" .................名稱對應................ """
# 使用參數名稱對應

""" def divide(n1, n2):
    print(n1/n2)

divide(2, 4)
divide(n2=2,n1=4) """

""" .................無限資料................ """
# 無限/不定資料
def avg(*ns):
    sum=0
    for n in ns:
        sum+=n
    print(sum/len(ns)) #ns=Tuple
        

avg(3,4)
avg(3, 4,15,15,456)
avg(3, 4, 15, 15, 4, 15, 15, 4, 15, 15)
