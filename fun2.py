def calculation(no1,no2):
	sum=no1+no2
	sub=no1-no2
	pro=no1*no2
	div=no1*no2
	return sum,sub,pro,div
res=calculation(10,2)
print(res)
print(type(res))
for no in res:
	print(no)
