# Write a program to read through a file and print the contents of the file (line by line) all in upper case

file_name = 'C:\\Projects\\Introduction-To-Python\\Day2\\mbox.txt'

file_handle = open(file_name)

for line in file_handle:
    print("Line in Upper : ", line.upper())