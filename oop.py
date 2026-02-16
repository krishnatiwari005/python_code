# class students:
#     name="krishna tiwari"
#     branch="cse"

# obj=students()
# print(obj.name)
# print(obj.branch)









# class car:
#     colors="blue"

# car1=car()
# print(car1.colors)







# class student:
#     #  def __init__(self):
#     #    pass 
     
#      def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("creating new students in data base")


# ob=student("mahi",99)
# print(ob.name,ob.marks)

# s=student("arjun",45)
# print(s.name,s.marks)







# class student:
#      college_name="akgec"
#      name="kuch ni"
#      def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("creating new students in data base")


# ob=student("mahi",99)
# print(ob.name,ob.marks)

# s=student("arjun",45)
# print(s.name,s.marks)
# print(student.college_name)












# class student:
#      college_name="akgec"
#      name="kuch ni"
#      def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("creating new students in data base")
#      def welcome(self):
#       print("bye bye",self.name)
#      def get_marks(self):
#         return self.marks

# ob=student("mahi",99)
# print(ob.name,ob.marks)

# ob.welcome()
# print(ob.get_marks())

















class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def hello():
        print("hello")
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your avg score is:",sum/3)
s1=student("krishna",[67,87,56])
s1.get_avg()
s1.hello()

s1.name="rahul"
s1.get_avg()
