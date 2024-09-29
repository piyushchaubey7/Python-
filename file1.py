f=open("abc.txt","r")
print("file name:", f.name)
print("file openin made:",f.mode)

print("is file readble:",f.readable())
print("is file writable:",f.writable())
print("is file closed:",f.closed)
f.close();
print("is file closed:",f.closed)
