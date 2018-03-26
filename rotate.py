# -*- coding: utf-8 -*-

import xlrd
import xlwt
def rotate(filename):
	data = xlrd.open_workbook(filename)
	new_table = xlwt.Workbook(encoding='utf-8')
	data_sheet = new_table.add_sheet('rotate')
	table = data.sheets()[0]
	rowcount = table.nrows
	
	colons = table.ncols
	
	rows = []
	
	
	for m in range(0,rowcount):
		cols = []
		for i in range(0,colons):	
			cols.append(table.cell(m,i).value)
		rows.append(cols)	
			#
	rotate_item = []
	for item in rows:
		item.reverse()
		rotate_item.append(item)
	num_rows = len(rotate_item[0])
	num_cols = len(rotate_item)
	for t in range(0,num_rows):
		for s in range(0,num_cols):
			data_sheet.write(t,s,rotate_item[s][t])
	
	new_table.save("rotate.xls")
	


if __name__ == "__main__":
	rotate("new.xlsx")