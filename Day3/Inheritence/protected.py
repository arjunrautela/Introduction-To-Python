class C :
    a = 'public class attr'
    _a = 'protected class attr'
    __a = 'private class attr'
    def __init__(self) :
        print ('obj constr')
        self.x = 'public instance attr'
        self._x = 'protected instance attr'
        self.__x = 'private instance attr'
        self.__x_ = 'aaaaaaa'


o = C()
print(o._C__x)
#print(C._C__a)
#print (C.__dict__)
print (o.__dict__)
