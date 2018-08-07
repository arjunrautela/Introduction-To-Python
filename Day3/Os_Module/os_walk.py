import os

print('os.walk: ', os.walk('C:\\Projects\\Introduction-To-Python\\Day3'))


for (root, dirs, files) in os.walk('C:\\Projects\\Introduction-To-Python\\Day3'):
    print('root : ', root)
    print('dirs : ', dirs)
    print('files : ', files)