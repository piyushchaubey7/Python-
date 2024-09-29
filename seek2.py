
f=open("abc1.txt","r+")
print("the current cursor position=",f.tell())
f.seek(5)
print("the current cursor position=",f.tell())
f.weite("java");
print(f.read())
print("the current cursor position=",f.tell())
f.seek(0)
print("the current cursor position=",f.tell())
print("data after modificattion")
print("f.read())



f.close()


