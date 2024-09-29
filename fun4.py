def add(no1,no2):
	print("Addtion=",no1+no2)

sum=add
add(10,2)
sum(20,5)
del add
sum(30,5)