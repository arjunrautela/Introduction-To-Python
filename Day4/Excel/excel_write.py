import xlwt
'''
Create a workbook
'''
workbook = xlwt.Workbook()

'''
Add a sheet
'''
worksheet = workbook.add_sheet('My_Sheet')

'''
Write content to cell
'''
worksheet.write(0,0, label='Row 0 and Coloumn 0 Value')
worksheet.write(1,1, label='Row 1 and Coloumn 1 Value')

'''
Save the file
'''
workbook.save('Excel_workbook.xls')
