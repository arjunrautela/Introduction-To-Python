import xlrd

file_name = "Sub_Task_Template.xlsx"

'''
Open Excel file and Read
'''
book = xlrd.open_workbook(file_name)

'''
Number of Sheet
'''
print(book.nsheets)

'''
Print sheet names
'''
print( book.sheet_names())

'''
Get Sheet by Index
'''
first_sheet_by_index = book.sheet_by_index(0)
print (first_sheet_by_index)
'''
Get Sheet by name
'''
sheet_by_n = book.sheet_by_name('Sheet1')
print (sheet_by_n)

'''
Get number of rows and coloumn from the sheet
'''
print (first_sheet_by_index.nrows)
print (first_sheet_by_index.ncols)

'''
Read a row and coloumn using index
'''
print (first_sheet_by_index.row_values(0))

print (first_sheet_by_index.col_values(0))

'''
Read Cell Data
'''
cell = first_sheet_by_index.cell(2,2)
print (cell.value)