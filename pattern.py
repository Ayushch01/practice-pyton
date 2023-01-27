     #1st
     
# n= int(input("enter your number"))
# for i in range (1,n+1):
#     i=" * "*i
#     print(i)

    #2nd

n=int(input("enter your number "))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")