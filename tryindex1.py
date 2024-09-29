print("code start...")

try:
	no1=int(input("Enter the first no"))
	no2=int(input("Enter the second no"))
	res=no1/no2
	str="hello"
	print(str[8]);
	print("try finished")
except ZeroDivisionError as msg:
	print("Exception description:",msg);
except indexError as msg:
	print("Exception description",msg);
print("code end")
