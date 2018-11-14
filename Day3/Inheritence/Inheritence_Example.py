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
        print(self.getName())
        return False
 
# Inherited or Sub class (Note Person in bracket)
class Employee(Person):
    
    def __init__(self, name ,dept):
        Person.__init__(self,name)
        self.dept = dept
    
    # Here we return true
    '''
    def isEmployee(self):
        return True
    '''
#emp = Person('Person1')
#print('Emp Name : ', emp.getName(), '\nisEmployee : ', emp.isEmployee())
class Dummy:
    pass
emp1 = Employee('Person2', 'MFS')

print(emp1.__dict__)
print(isinstance(emp1, Person))
print(isinstance(emp1,Dummy))
#per = Person('Person1')
#print(per.__dict__)
#print(emp1.isEmployee())
#emp1 = Employee('Person2')
#emp1 = Employee()

#print('Emp Name : ', emp1.getName(), '\nisEmployee : ', emp1.isEmployee())
