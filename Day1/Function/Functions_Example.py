#Function example

#The function object may be assigned to other names
def sum(a,b):
    return a+b

def mul(a,b):
    return a*b

print ("Mul : ", mul(2,3))

x = mul
print("X Mul : ", x(2,3))

# List consisting of function name
func_list = [sum, mul]
print(func_list[0](2,3))