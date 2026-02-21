#single inheritance

# class car:
#     color="black"
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class toyotacar(car):
#     def __init__(self,name):
#         self.name=name
# car1=toyotacar("fortuner")
# car2=toyotacar("bmw")

# print(car1.start())
# print(car1.color) 















#multi level inheritance

# class car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class toyotacar(car):
#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(toyotacar):
#     def __init__(self, type):
#         self.type=type

# car1=Fortuner("deisel")
# car1.start()







#multiple inheritance

# class A:
#     varA="Welcome to class A"

# class B:
#     varB="Welcome to class B"

# class C(A,B):
#     varC="Welcome to class C"

# c1=C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)










# class car:

#     def __init__(self,type):
#         self.type=type

#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class toyotacar(car):
#     def __init__(self,brand,type):
#         self.brand=brand
#         super().__init__(type)
#         super().start()



# car1=toyotacar("bmw","electric")
# print(car1.type)















# class person:
#     name="anonymous"

#     # def changeName(self,name):
#     #     # person.name=name
#     #     self.__class__.name="krishna tiwari"
#     @classmethod
#     def changeName(cls,name):
#         cls.name=name


# p1=person()
# p1.changeName("krishna")
# print(p1.name)
# print(person.name)



















class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math


        #self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
    # def calcpercentage(self):
    #     self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
    
    
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%" 

stu1=student(78,89,99)
print(stu1.percentage)      

stu1.phy=56
print(stu1.percentage)  