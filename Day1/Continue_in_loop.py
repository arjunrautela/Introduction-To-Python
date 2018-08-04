#Usage of continue in loops

#Continue in for loop

name = 'Captain'

for ch in name:
    if ch == 'p':
        continue
    print("Ch is : ", ch)
else:
    print("For loop exit")


#Continue in while loop

index = 0
while index < len(name):
    
    if name[index] == 'p':
        index = index + 1
        continue
    print("Ch is : ", name[index])
    index = index + 1
else:
    print('While loop exit')