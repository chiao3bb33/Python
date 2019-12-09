# 載入內建的sys模組並取得資訊
""" import sys as system
print(system.platform)
print(system.maxsize) """

# 建立geometry模組,載入使用
""" import geometry as geo
x = geo.distance(1, 2, 5, 3)
print(x)
x = geo.slope(1, 2, 5, 3)
print(x) """

# 調整搜尋模組的路徑
""" import sys as s
s.path.append("Modules")  # 在模組的搜尋路徑列表中【新增路徑】
print(s.path)  # 印出模組的搜尋路徑列表
print('-------------------')

import geometry
print(geometry.distance(1, 2, 5, 3)) """
