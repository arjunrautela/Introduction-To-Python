# Calculator Module
#print('Executing Calculator Module')
print('__name__ : ', __name__)

name = "Calculator"
__name = "New Calculator"

def sum(x,y):
    return x+y

def diff(x,y):
    return x-y

def prod(x,y):
    return x*y

def power(x,y):
    return x**y

if __name__ == "__main__":
    print ('Hello Calculator')
    print("name : ", name)