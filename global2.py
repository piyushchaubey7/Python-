a=10
def fun1():
	a=20
	print("local a=",a)
	print("global a=",globals()['a'])

def fun2():
	print("global a=",a)
fun1()
fun2()


	