#Function having default arguments
'''
Function for split the string on a given character, default is space
'''
def func_def_args(str_data, delim = ' '):
    print(str_data.split(delim))

data = 'The quick brown fox jumps over the lazy dog'
func_def_args(data, 'f')

