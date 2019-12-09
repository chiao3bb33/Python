#定義類別，與類別屬性(封裝載類別中的變數和函數)
#TYPE A
""" #定義一個類別 IO ， 有兩個屬性 supportedSrcs 和 read
class IO:
    supportedSrcs=["console","file"]
    def read(src):
        print('read from',src)
#使用類別
print(IO.supportedSrcs)
IO.read('file')  #呼叫類別中的屬性＿函式 """

#TYPE B
#定義一個類別 IO ， 有兩個屬性 supportedSrcs 和 read
class IO:
    supportedSrcs=["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print('!!Not Supported!!')
        else:
            print('read from',src)
#使用類別
print(IO.supportedSrcs)
IO.read('file')  #呼叫類別中的屬性＿函式
IO.read('internet')  #放入不資源的列表 判斷