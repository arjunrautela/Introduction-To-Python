#Usage of Break in For loop

name = 'Captain'

#Break Example in for loop

for ch in name:
    if ch == 'x':
        break
    print ("Ch is : ", ch)
else:
    print("For Loop exit")

#Break Example in while loop

index = 0
while index < len(name):
    if name[index] == 'i':
        break
    print("Ch is : ", name[index])
    index = index + 1
else:
    print("While Loop Exit")