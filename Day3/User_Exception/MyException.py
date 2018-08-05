# Custom Exception class

class myException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

try:
    raise(myException('Something wrong happen'))
except myException as myexcp:
    print(myexcp)