# -*- coding: utf-8 -*-

import xlrd
import xlwt

def rotate(filename):
	
	data = xlrd.open_workbook(filename)  #读取原始xls或xlsx表格
	
	new_table = xlwt.Workbook(encoding='utf-8')  #定义输出excel文件
	data_sheet = new_table.add_sheet('rotate')   #定义输出表格的工作表
	table = data.sheets()[0]  #读取原始xls的第一张工作表
	rowcount = table.nrows    #获取原始表格数据的行数和列数
	colons = table.ncols
	
	rows = []
	
	
	for m in range(0,rowcount):
		cols = []
		for i in range(0,colons):	
			cols.append(table.cell(m,i).value)
		rows.append(cols)	
		#将原始表格数据存入列表（二维）
	rotate_item = []
	for item in rows:
		item.reverse()
		rotate_item.append(item)
		#通过reverse函数将列数据倒序排列
	num_rows = len(rotate_item[0])
	num_cols = len(rotate_item)
	for t in range(0,num_rows):
		for s in range(0,num_cols):
			data_sheet.write(t,s,rotate_item[s][t])
			#重新生成excel表格
	new_table.save("rotate.xls")
	#保存xls文件


if __name__ == "__main__":
	rotate(filename)  #输入文件名
