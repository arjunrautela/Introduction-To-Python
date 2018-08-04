# Find the count of character in a string

name = 'Mississippi'

count = {}

for ch in name:
    if ch not in count:
        count[ch] = 1
    else:
        count[ch] = count[ch] + 1

print("Count : ", count)


#With using get
count1 = {}
for ch in name:
    if ch not in count1:
        count1[ch] = count1.get(ch,1)
    else:
        count1[ch] = count1.get(ch,1) + 1
print("Count1: ", count1)