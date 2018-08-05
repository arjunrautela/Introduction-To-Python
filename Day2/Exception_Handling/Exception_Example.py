# Example of Exception in python

'''
Function 
'''
def func(a, b) :
    if b > len(a)-1 :
        print('wrong index')
        raise IndexError		#raise exception
    return a[b]

a = 'asdf'
try :
    print('# 1')
    func(a, 1)
    print('# 2')
    #func(a, 10)
    print('# 3')
    func(a, 2)
except IndexError :
    print('error')
else:
    print('Executing else block')
finally:
    print('Executing finally block')
print('After the try catch block')

