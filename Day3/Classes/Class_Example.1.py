# Class Example without the constructor

class Calculator:
    '''
    Calculator Class Without __init__ function
    '''
    calcClassVar = 0
    def sum(self, num1, num2):
        return num1 + num2
    
    def prod(self, num1, num2):
        return num1 * num2

if __name__ == "__main__":
    calc = Calculator()
    print('Sum : ' , calc.sum(1,3))
    print('Prod : ' , calc.prod(4,3))
    print('calc.__dict__ : ', calc.__dict__)
    print('Calculator.__dict__ : ', Calculator.__dict__)
    