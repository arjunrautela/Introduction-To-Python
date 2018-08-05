# Contains example of Nested Scope.

name = 'This is a global name'

def greet():
    # Enclosing function
    #name = 'Sammy'
    
    def hello():
        #name  = "Arjun"
        print('Hello '+name)
    
    hello()

greet()



x = 50

def func1(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func1(x)
print('x is still', x)



x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)


