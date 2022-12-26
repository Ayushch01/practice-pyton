def calculator(num1,num2,choice):
	if choice=="+":
		result=num1+num2
		return result
	elif choice=="-":
		result=num1-num2
		return result
	elif choice=="*":
		result=num1*num2
		return result
	else:
		result=num1/num2
	return result
a=float(input("enter your first value"))
b=float(input("enter your second value"))
c=input("enter the operation(+,-,*,/):")
d=calculator(a,b,c)
print(d)
