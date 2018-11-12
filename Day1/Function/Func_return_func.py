# Example for function returning a funciton
'''
def base_func(a):
    print("Argument a : ", a)
    def inner_func(b):
        print("Inner Func : ", b)
    inner_func(4)
    return inner_func

ret_func = base_func(2)
print('type : ', type(ret_func))

ret_func(3)
'''
def my_sum(a,b):
    return a+b

def main(my_sum_arg):
    print(my_sum_arg(2,3))

main(my_sum)
