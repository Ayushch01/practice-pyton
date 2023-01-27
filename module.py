# import time
# import time as t
from time import *

fac1=int(input("enter your number"))
start_time=time()
y=1
for i in range(1,fac1+1):
	y=y*i
print(y)

end_time=time()
total=end_time-start_time
print(total)