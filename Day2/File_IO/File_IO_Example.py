# File I/O Example
# Read a Txt file.

file_name = 'C:\\Projects\\Introduction-To-Python\\Day2\\mbox.txt'

file_handle = open(file_name)

#print('All Lines :', file_handle.readlines())

#print('Read() : ', file_handle.read())

print('readline : ',file_handle.readline()) 

# print each line:
for line in file_handle:
    print (line)