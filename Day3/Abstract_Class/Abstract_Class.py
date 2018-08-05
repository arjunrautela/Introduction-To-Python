# Abstract class in python example
# https://www.python-course.eu/python3_abstract_classes.php

from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
    def __init__(self,value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_somethinig(self):
        pass

class subclass(AbstractClassExample):
    def __init__(self, value):
        self.value = value
        super().__init__(value)
    def do_somethinig(self):
        print(self.value)

x = subclass(4)
x.do_somethinig()