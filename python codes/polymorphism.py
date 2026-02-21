class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show(self):
        print(self.real,"i+",self.img,"j")
    # def add(self,num2):
    #     newreal=self.real+num2.real
    #     newimg=self.img+num2.img
    #     return complex(newreal,newimg)
    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return complex(newreal,newimg)
    def __sub__(self,num2):
        newreal=self.real-num2.real
        newimg=self.img-num2.img
        return complex(newreal,newimg)
    def __mul__(self,num2):
        newreal=self.real*num2.real
        newimg=self.img*num2.img
        return complex(newreal,newimg)
    def __mod__(self,num2):
        newreal=self.real%num2.real
        newimg=self.img%num2.img
        return complex(newreal,newimg)
num1=complex(1,3)
num1.show()

num2=complex(5,6)
num2.show()

# num3=num1.add(num2)
# num3.show()

num3=num1+num2
num3.show()
num3=num1-num2
num3.show()
num3=num1*num2
num3.show()
num3=num1%num2
num3.show()