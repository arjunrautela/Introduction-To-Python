# Example of function variable args.

def func_var_args(*args):
    print(type(args))
    total = 0
    for item in args:
        total = total + item
    print("Total : ", total)


func_var_args(1,2,3,4,5,6)

func_var_args(1,2)
func_var_args(1,2,3,4)