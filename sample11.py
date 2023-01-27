def fact(x):
    num1=1
    if x==0 and x==1:
        return num1
    else:
        for i in range(1,x+1):
            num1*=i                  
    return num1
