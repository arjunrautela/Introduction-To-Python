#l = ['abc@gmail.com', 'aaaio@gmail.com']   create list with only user names - ['abc', 'aaa']
l = ['abc@gmail.com', 'aaaio@gmail.com'] 

name_list = []

for item in l:
    name_list.append(item.split('@')[0])

print("name list : ", name_list)
