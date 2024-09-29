def square(no):
	return no*no
def cube(no):
	return no*no*no
s=square

print(id(square))
print(id(s))
print(id(cube))