#Describing how arguments are passed to function

## Immutable object passed to function arguments.
'''
def sum(a,b):
    print("Id of a :", id(a))
    print("Id of b :", id(b)) 
    a = 20
    print("Id of a after update:", id(a))
    total = a + b
    return total

x = 5
y = 10

print("Id of x : ", id(x))
print("Id of y : ", id(y))

sum_x_y = sum(x,y)
print('Sum of x and y', sum_x_y)
'''


## Mutable object passed to it
# function that accept list as input and append a value to it

def list_func(name_list):
    print("id of name_list : ", id(name_list))
    print("Original List : ", name_list)
    name_list.append('Kevin')

min_name = ['Bob', 'stuart']
print("Id of min_name : ", id(min_name))

list_func(min_name)
print("min_name list after function call : ", min_name)
