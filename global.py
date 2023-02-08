def myfunction():
    global i
    x=int(input("enter value :"))
    y=int(input("enter value :"))
    z=x+y
    print(z)
    i="i am inside"


i="I am fine"
print(id(i))  
print(i)            #global variable
myfunction()
print(i)
#print(z)            #being z a local variable it cant accessed outside myfunction