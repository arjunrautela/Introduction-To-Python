#Loop Example in python

#For Loop

name = 'Arjun'

for ch in name:
    print("Ch : ", ch, end='\t')
else:
    print("\nFor loop is finished")


#While loop Example:
index = 0
while index < len(name):
    print("Ch : ", name[index])
    index = index + 1
else:
    print("While loop Finished")
    print("While Loop Ends")