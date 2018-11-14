# Custom Exception class

class myException(Exception):
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return "Following Excepiton : " + self.value
    

if __name__ == "__main__":
    try:
        #raise(myException('Something wrong'))
        raise Exception('Some thing wrong')
        #raise myException
    except Exception as myexp:
        print(myexp)