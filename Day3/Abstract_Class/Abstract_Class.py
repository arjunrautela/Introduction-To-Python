# Abstract class in python example
# https://www.python-course.eu/python3_abstract_classes.php

from abc import ABC, abstractmethod, abstractproperty

class AbstractClassExample(ABC):
    def __init__(self,value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_somethinig(self):
        pass
    @abstractproperty
    def abs_value(self):
        pass


class subclass(AbstractClassExample):
    def __init__(self, value):
        self.value = value
        super().__init__(value)
    
    def do_somethinig(self):
        print(self.value)
    
    @property
    def abs_value(self):
        return 'concrete property'

 
x = subclass(4)
x.do_somethinig()
print("x.value : ", x.abs_value)