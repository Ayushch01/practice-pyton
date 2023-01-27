user_input1= input("enter the  first Numeric value you wanna perform operation: ")
user_input2= input("enter the  second Numeric value you wanna perform operation: ")

### checking the given input by user wheater it is Int or Float
def check(user_input1):
	num_char=["0","1","2","3","4","5","6","7","8","9"]

	num_count = 0
	dot_count = 0
	
	for i in user_input1:
		if i in num_char:
			num_count += 1
		elif i == ".":
			dot_count += 1
		
	if  dot_count ==0:
		user_input1 = int(user_input1)

	elif   dot_count ==1:
		user_input1 = float(user_input1)
	
	return user_input1

user_input1 = check(user_input1)
print(type(user_input1))

user_input2 = check(user_input2)
print(type(user_input2))

print()
print("press  Numbers according to your choice : ")
print()
print(""" press the operation you Wanna perfor
             +       -
             *       /""") 

### for full value
def con(b):
    temp1 = int(b)
    temp2  = b-temp1
    if temp2 <= 0:
        b =int(b)
    else:
        b = float(b) 
    return b

### operations to be performed
def add(x,y):
    z = x+y
    print(z)
def sub(x,y):
    z = x-y
    print(z)
    
def mul(x,y):
    z = x*y
    print(z)
def div(x,y):
    if user_input2 == 0:
        print("Divisor vala number zero h me operation nahi krega ")
    else:    
        z = x/y
        c = con(z)
        print(c)

### user choice 
choice = input("enter your choice: ")
if choice == '+':
    add(user_input1,user_input2)
    
elif choice == "-":
    sub(user_input1,user_input2)
    
elif choice == "*":
   mul(user_input1,user_input2)
   
elif choice == "/":
    div(user_input1,user_input2)
else:
    print("invalid choice")