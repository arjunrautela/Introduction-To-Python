import xlrd

file_name = "C:\\Projects\\Introduction-To-Python\\Day4\\Excel\\Sub_Task_Template.xlsx"

'''
Open Excel file and Read
'''
book = xlrd.open_workbook(file_name)

'''
Number of Sheet
'''
print('Number of Sheets : ', book.nsheets)

'''
Print sheet names
'''
print('Print Sheet names : ', book.sheet_names())

'''
Get Sheet by Index
'''
first_sheet_by_index = book.sheet_by_index(0)
print ('First sheet by Index : ', first_sheet_by_index)
'''
Get Sheet by name
'''
sheet_by_n = book.sheet_by_name('Sheet1')
print ('Sheet by Name : ', sheet_by_n)

'''
Get number of rows and coloumn from the sheet
'''
print ('Number of Rows : ', first_sheet_by_index.nrows)
print ('Number of Columns : ', first_sheet_by_index.ncols)

'''
Read a row and coloumn using index
'''
print ('First Row : ', first_sheet_by_index.row_values(0))

print ('First Column : ', first_sheet_by_index.col_values(0))

'''
Read Cell Data
'''
cell = first_sheet_by_index.cell(2,2)
print ('Cell Data (2,2) : ', cell.value)