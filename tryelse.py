
print("code start...")
no1=no2=0

try:
	no1=int(input("Enter the first no"))
	no2=int(input("Enter the second no"))
	res=no1/no2
	
except ZeroDivisionError as msg:
	print("Exception description:",msg);
else:
	print("Division=",res)
fianlly:
	print("finally block executed");

print("code end")