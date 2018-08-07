# Custom Exception class

class myException(Exception):
    '''
    def __init__(self, value):
        self.value = value
    '''
    def __str__(self):
        return 'Something wrong happen'
    
    pass
try:
    #raise(myException('Something wrong happen'))
    raise myException
except myException as myexcp:
    print(myexcp)