# Custom Exception class

class myException(Exception):
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return self.value
    

if __name__ == "__main__":
    try:
        raise(myException('Something wrong'))
        #raise myException
    except myException as myexp:
        print(myexp)