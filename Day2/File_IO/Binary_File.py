# Example of Binary File:
#https://www.devdungeon.com/content/working-binary-data-python
import os

print(os.curdir)

file_name = 'C:\\Projects\\Introduction-To-Python\\Day2\\File_IO\\User_Input.py'
#file_name = 'myfile.bin'
f = open(file_name, "rb")

print(f.read(1))

f.close()