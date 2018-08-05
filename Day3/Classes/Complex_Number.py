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

    def __del__(self):
        print("Deleting the object : ", self)

if __name__ == "__main__":
    c1 = Complex_Num(2,3)
    c2 = Complex_Num(3,4)

    c3 = c1 + c2

    print(c3)