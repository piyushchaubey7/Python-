
print("code start...")

try:
	no1=int(input("Enter the first no"))
	no2=int(input("Enter the second no"))
	res=no1/no2
	
except ZeroDivisionError as msg:
	print("Exception description:",msg);
try:
       str="hello"
       print(str[8]);
       print("try finished")
except indexError as msg:
	print("Exception description",msg);

print("code end")
