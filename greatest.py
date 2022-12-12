num1=int(input("Enter num1= "))
print(type(num1))
num2=int(input("Enter num2= "))
print(type(num2))
num3=int(input("Enter num3= "))
print(type(num3))


if (num1>=num2) and (num1>=num3):
	print(num1, "is greatest")

elif (num2>=num1) and (num2>=num3):

   	print(num2, "is greatest")

else:
	print(num3, "is greatest")