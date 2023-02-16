# class test:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def show(self):
#         print("part a :",self.a)
#         print("part b :",self.b)
#     def __add__(self,other):
#         x=self.a+other.a
#         y=self.b+other.b
#         z=test(x,y)
#         return z    

# s1=test(24,25)
# s2=test(45,50)
# s3=s1+s2
# s3.show()
a=5
b=6
c=a.__add__(b)
print(c)
