def iseven(no):
	if no%2==0:
		return True
	else:
		return False
l1=[0,5,10,7,15,20,9]
l2=list(filter(iseven,l1))
print(l2)