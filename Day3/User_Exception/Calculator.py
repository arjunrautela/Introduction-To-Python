from MyException import myException

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def sum(self):
        if (isinstance(self.num1, int) and isinstance(self.num2, int)):
            return self.num1 + self.num2
        else :
            raise myException('Error Occured')

if __name__ == "__main__":
    calc = Calculator('2','3')
    #print(dir(Calculator))
    try:
        print('Sum : ', calc.sum())
    except myException as exp:
        print("Exception : ", exp)
        print(exp.__class__)