# Example for function returning a funciton

def base_func(a):
    print("Argument a : ", a)
    def inner_func():
        print("Inner Func")
    return inner_func

ret_func = base_func(2)

ret_func()