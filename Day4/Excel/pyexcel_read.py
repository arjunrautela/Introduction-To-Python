import pyexcel as p
records = p.iget_records(file_name='Sub_Task_Template.xlsx', sheet_name= 'Sheet1')
for record in records:
    print('fd ', record['Project'])