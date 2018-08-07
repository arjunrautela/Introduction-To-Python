# Inheritence Example

class emp:
    def __init__(self, val):
        self.val = val
    
    def display(self):
        print(self.val)


class special_emp(emp):
    def display(self):
        print('I am a special emp', self.val)


if __name__ == "__main__":
    sp_emp = special_emp('Arjun')
    sp_emp.display()