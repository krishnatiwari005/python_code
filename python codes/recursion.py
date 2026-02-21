# def show(n):
#     if(n==0):
#         return 
#     print(n)
#     show(n-1)
# show(10)


# def fac(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fac(n-1)
    
# n=int(input("enter a number : "))
# a=fac(n)
# print(a)




# def calc(n):
#     if(n==0):
#         return 0
#     return n+calc(n-1)
# print(calc(3))


 
def print_list(list,ind=0):
    if(ind==len(list)):
        return
    print(list[ind])
    print_list(list,ind+1)

names=["abc","pqr","rst"]

print_list(names)
