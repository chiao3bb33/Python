""" 
#建立類別
#定義初始化函式
#建立實體屬性
#建立實體方法
#函式作用的功能
#建立實體物件
#呼叫實體方法 
"""
#Point 實體物件的設計：平面座標上的點

""" class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #定義實體方法(可多個)
    def show(self):
        print(self.x, self.y)
    def distance(self,targetX, targetY):
        return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5
p=Point(3,4)
p.show() #呼叫實體方法/函式
result=p.distance(0,0) #計算3,4和坐標0,0之間的距離
print(result) """

#File 實體物件的設計：包裝檔案讀取的程式
class File:
    #定義初始化函式
    def __init__(self,name):
        #建立實體屬性
        self.name=name
        self.file=None #尚未開啟檔案： 初期是None (Python特殊資料 代表空)
    #定義實體方法
    def open(self):   
        #self.file＝實體屬性 (把函式功能放進實體屬性裡面)
        #FF
        self.file=open(self.name, mode='r',encoding='utf-8') #Python內建開啟檔案的函式
    def read(self):
        #GG
        return self.file.read()
#以上設計完一個實體物件

#讀取第一個檔案
f1=File('for26data1.txt') #File(XXXX)=呼叫初始化函數 #建立實體物件 放在變數f1 將初始化函數放在f1
f1.open() #利用變數f1代表實體物件.呼叫實體方法open 就會跑上面#FF的code
data=f1.read() #接著呼叫實體方法read 就會跑上面#GG的code 然後放在變數"data"
print(data)    #印出
#2讀取第二個檔案
f2=File('for26data2.txt')
f2.open()
data=f2.read()
print(data)