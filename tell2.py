f=open("abc.txt","r")
print("total byte of the file:",f.tell())
print(f.read(2))
print("total byte of the file:",f.tell())
print(f.read(3))
print("total byte of the file:",f.tell())
print(f.read(1))

print("total byte of the file:",f.tell())



