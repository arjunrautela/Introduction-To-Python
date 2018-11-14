# Decorator Example

def my_decorator(some_function):

    def wrapper(*args, **kwargs):
        print("Something is happening before some_function() is called.")

        some_function(*args, **kwargs)

        print("Something is happening after some_function() is called.")
    return wrapper

@my_decorator
def just_some_function(x,y):
    print('Sum : , ',  x +y)

just_some_function(2,4)

#just_some_function = my_decorator(just_some_function, 2,4)

#just_some_function(2,4)