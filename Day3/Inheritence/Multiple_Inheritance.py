# Example of Multiple Inheritance

class base1:
    def __init__(self, b1):
        self.b1 = b1
    
    def display(self):
        print('Display b1 : ', self.b1)


class base2:
    def __init__(self, b2):
        self.b2 = b2
    
    def display(self):
        print('Display 2 : ', self.b2)


class derived(base2, base1):
    def __init__(self, d1, b1, b2):
        base1.__init__(self,b1)
        base2.__init__(self,b2)
        self.d1 = d1
    '''
    def display(self):
        print('Derived display : ', self.d1)
    '''
if __name__ == "__main__":
    #b1 = base1(20)

    d = derived(13,14,15)
    d.display()