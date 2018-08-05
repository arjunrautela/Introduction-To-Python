#s = 'axb'   create list of characters as follows :	['b'. 'y', 'c']. 

name = 'axb'

name_list = []
for ch in name:
    name_list.append(chr(ord(ch)+1))

print("Final List : ", name_list)
