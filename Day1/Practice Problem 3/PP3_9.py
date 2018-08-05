#l = ['abc@gmail.com', 'aaa@gmail.com', 'abc@yahoo.com']   create a collection of unique email service providers  

l = ['abc@gmail.com', 'aaa@gmail.com', 'abc@yahoo.com']

email_sp = set()

for name in l:
    email_sp.add(name.split('@')[1].split('.')[0])

print("Unique service provider : ", email_sp)