# Inhertance Example :
class Person:
    # Constructor
    def __init__(self, name):
        self.name = name
 
    # To get name
    def getName(self):
        return self.name
 
    # To check if this person is employee
    def isEmployee(self):
        return False
 
 
# Inherited or Sub class (Note Person in bracket)
class Employee(Person):
    '''
    def __init__(self, name ,dept):
        Person.__init__(self,name)
        self.dept = dept
    '''
    # Here we return true
    def isEmployee(self):
        return True

emp = Person('Person1')
print('Emp Name : ', emp.getName(), '\nisEmployee : ', emp.isEmployee())

#emp1 = Employee('Person2', 'MFS')
emp1 = Employee('Person2')

print('Emp Name : ', emp1.getName(), '\nisEmployee : ', emp1.isEmployee())
