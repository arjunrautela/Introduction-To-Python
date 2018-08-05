# Class Example

class Employee:
    strOganization = 'Gemalto'
    intEmpCount = 0

    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        Employee.intEmpCount += 1


if __name__ == "__main__":
    emp1 = Employee('Arjun', '10033567')
    emp2 = Employee('Rautela', '10033568')
    print('Employee Count : ', Employee.intEmpCount)