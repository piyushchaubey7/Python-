def outer():
	 print("outer method start=")
	def inner():
		print("inner method execute")
	print("outer method ends..");
	inner()
outer()
