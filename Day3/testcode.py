i = 3
with open('arjun.txt','w') as file_open:
    i = 0
    print('id of i = 0 : ', id(i))
    y = 0
    if y == 0:
        i = i + 2
        print('id of i after update : ', id(i))
print ('id of i  :', id(i))
print('value of i : ', i)