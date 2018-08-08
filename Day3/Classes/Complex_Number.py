# Complex number class

class Complex_Num:
    def __init__(self, real, img):
        self.real = real
        self.img = img
 
    def __str__(self):
        return 'Complex Number is {} + i{}'.format(self.real, self.img)
    
    def __add__(self, obj):
        new_real = self.real + obj.real
        new_ing = self.img + obj.img
        return Complex_Num(new_real, new_ing) 
    
    def __getitem__(self,item):
        print('In Get Item', item)
        if item == 0:
            return self.real
        else:
            return self.img
    
    def __setitem__(self, item, value):
        print('In Set Item : ', item)
        if item == 'real':
            self.real = value
        else:
            self.img = value

    def __del__(self):
        print("Deleting the object : ", self)

if __name__ == "__main__":
    c1 = Complex_Num(2,3)
    c2 = Complex_Num(3,4)

    print('Real of C1 : ', c1[0])
    print('Update Img part of C1 : ')
    c1['real'] = 10
    print ('Updated C1 : ', c1)
    c3 = c1 + c2

    print(c3)
    del c3