# import sample11
import sample11 as s
#calculating permutation
n,r=int(input("enter value of n : ")),int(input("enter value of r : "))
if n>=r:
    result=s.fact(n)/s.fact(n-r)
    print(result)
else:
    print("n should be greater than r...correct it..!!!")

#calculating combination
p,c=int(input("enter value of p : ")),int(input("enter value of c : "))
if p>=c:
    result=s.fact(p)/(s.fact(c)*s.fact(p-c))
    print(result)
else:
    print("n should be greater than r...correct it..!!!")