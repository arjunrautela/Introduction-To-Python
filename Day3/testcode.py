i = 3
print('id of i=3 : ', id(i))
with open('arjun.txt','w') as file_open:
    i = 0
    print('id of i = 0 : ', id(i))
    y = 0
    if y == 0:
        print('id of i in y = 0 : ', id(i))
        i = i + 2
        print('id of i after update : ', id(i))
print ('id of i  :', id(i))
print('value of i : ', i)