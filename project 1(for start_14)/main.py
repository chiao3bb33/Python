#主程式
import geometry.point
result=geometry.point.distance(3,4)
print('距離',result)
import geometry.line
result=geometry.line.slope(1,1,3,3)
print('斜率',result)

#使用別名
import geometry.point as pp
result=pp.distance(3,4)
print('距離',result)
import geometry.line as li
result=li.slope(1,1,3,3)
print('斜率',result)