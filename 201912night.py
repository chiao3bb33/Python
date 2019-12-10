# 匯入 xlwings 套件
import xlwings as xw
# 讓 xlwings 動態開啟一個新的 Excel 檔案，並將該檔案存入 workbook 變數
workbook = xw.Book()
# 若你沒有開啟你的 Excel, 這行可能會跑的慢一點，請耐心等待，讓子彈飛一會兒～
""" # 到 workbook 代表的 excel 檔案下，開啓名爲 '工作表1' 的試算表
sheet = workbook.sheets['工作表1']
# 將該試算表裏面的 A1 儲存格的值設定成 "Hello World!"
sheet.cells(1, 1).value = "Hello World!" """

# 到 workbook 代表的 excel 檔案下，開啓名爲 '工作表1' 的試算表
sheet = workbook.sheets['工作表1']
# 和 VBA 的 Cells() 函數一樣，xlings 支援可以用英文字母指定欄！
sheet.cells(1,1).value = "Hello World!"
sheet.cells(2,2).value = '愛'