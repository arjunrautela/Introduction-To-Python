# Class Example

class Employee:
    '''
    Employee Class
    '''
    strOganization = 'Gemalto'
    intEmpCount = 0

    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        Employee.intEmpCount += 1
        
    
    def getEmpDetails(self):
        return "\nName : " + self.name +', \nId :' + self.emp_id


if __name__ == "__main__":
    emp1 = Employee('Arjun', '10033567')
    print('Employee Count : ', Employee.intEmpCount)
    
    '''
    emp1 = Employee('Arjun', '10033567')
    emp2 = Employee('Rautela', '10033568')
    emp3 = emp1
    print('Emp1 Name: ', emp1.name)
    print('Emp3 Name : ', emp3.name)
    print('Employee Count : ', Employee.intEmpCount)

    print('Emp1 Details ==> ', emp1.getEmpDetails())

    print('Employee.__dict__ : ', Employee.__dict__)
    print('emp1.__dict__ : ', emp1.__dict__)
    '''