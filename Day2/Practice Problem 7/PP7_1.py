# Count number of lines in txt file

file_name = 'C:\\Projects\\Introduction-To-Python\\Day2\\mbox.txt'

#file_handle = open(file_name)

count = 0
'''
for line in file_handle:
    count = count + 1
'''
with open(file_name) as with_handle:
    for line in with_handle:
        print('Line : ', line)

print("With : ", with_handle.closed)
print("Number of Lines : ", count)

#file_handle.close()
