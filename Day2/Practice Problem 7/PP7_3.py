#Write a program to prompt for a file name, and then read through the file and look for lines of the form: 
# 1. X-DSPAM-Confidence: 0.8475 and sum the value after 
# 2. Print all the line containing @ sign
# 3. Print all the lines starts with ‘From’
# 4. Read two numbers from the user and save the sum to a file.

import time
file_name = 'C:\\Projects\\Introduction-To-Python\\Day2\\mbox.txt'


file_handle = open(file_name)

total = 0.0
for line in file_handle:
    if line.startswith('X-DSPAM-Confidence'):
        num = float(line.split(':')[1].strip())
        total = total + num
        #time.sleep(2)
        print(total)
print('Total : ', total)


file_handle.seek(0)

for line in file_handle:
    if line.find('@') != -1:
        print(line)

file_handle.close()



