def outer():
	 print("outer method start=")
	def inner():
		print("inner method execute")
	print("outer method ends..");
	return inner()
outer()
f1=outer()
print(f1)
print(outer())