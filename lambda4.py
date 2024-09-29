def square(no):
	return no*no
l1=[1,2,3,4,5,6,7,8,9,10]
l2=list(map(square,l1))
print(l2)
l3=list(map(lambda X:X*X,l1))
print(l3)
l3=list(map(lambda x:2*X,l1))
print(l3)
