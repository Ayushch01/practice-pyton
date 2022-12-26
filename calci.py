num1=int(input("enter first number : "))
num2=int(input("enter second number : "))
choice=input("enter your choice")
if choice==chr(42):
	print("your multiplication is : ",num1*num2)
elif choice==chr(43):
	print("your addition is : ",num1+num2)
elif choice==chr(45):
	print("your substraction is : ",num1-num2)
elif choice==chr(47):
	print("your division is : ",num1/num2)
else:
	print("invalid input")