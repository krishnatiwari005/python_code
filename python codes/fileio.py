# f=open("demo.txt","r")
# data=f.read()
# print(data)
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# print(type(data))
# f.close()



# f=open("demo.txt","a")

# f.write("\nI want to learn python this sum only")

# f.close()




# f=open("sample.txt","a")
# f.close()






# f=open("sample.txt","a+")
# #f.write("abc")
# print(f.read())
# f.write("abc")
# f.close()




# with open("sample.txt","r") as f:
#     data=f.read()
#     print(data)

# with open("sample.txt","a") as f:
#     f.write("hahaha")







# import  os
# os.remove("sample.txt")



# with open("practice.txt","w") as f:
#     f.write("hi every one \n i love india ")
#     f.write("bye beye")





# with open("practice.txt","r") as f:
#     data=f.read()
# new_data=data.replace("bye","tata")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)




# def check(word):
    
#     with open("practice.txt","r") as f:
#      data=f.read()
#      if(data.find(word)!=-1):
#         print("found")
#      else:
#         print("not found")

# check("indiaj")




# def check(word):
#     data=True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return 
#             line_no+=1
#     return -1        
# print(check("india"))







with open("practice.txt","r") as f:
    data=f.read()
    print(data)

    # num=""
    # for i in range(len(data)):
    #     if(data[i]==","):
    #         print(int(num))
    #         num=""
    #     else:
    #         num+=data[i]


count=0
num=data.split(",")
for val in num:
    if(int(val)%2==0):
        count+=1

print(count)