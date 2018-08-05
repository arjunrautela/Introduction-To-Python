# Inheritance with __init__ example

class base:
    def __init__(self, b1):
        print('Base 1 : ', b1)

class der(base):
    def __init__(self, d1,b1):
        print('Derived init : ', d1)
        base.__init__(self,b1)

obj = der(2,3)
