# Example for function returning a funciton

def base_func(a):
    print("Argument a : ", a)
    def inner_func(b):
        print("Inner Func : ", b)
    inner_func(4)
    return inner_func

ret_func = base_func(2)
print('type : ', type(ret_func))

ret_func(3)