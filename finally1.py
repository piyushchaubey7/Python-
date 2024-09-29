import os
print("code start...")

try:
	no1=int(input("Enter the first no"))
	no2=int(input("Enter the second no"))
	res=no1/no2
	os._exit(0)
	print("try finished")
except ZeroDivisionError as msg:
	print("Exception description:",msg);
except indexError as msg:
	print("Exception description",msg);
except:
	print("Enter only valid input values");
finally:
	print("finally block");
print("code end")
