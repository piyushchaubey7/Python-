data=input("Enter data you want to write in file");
f=open("abc1.txt","w")
f.write(data)
f.close()
f=open("abc.txt","r")
f.seek(5)
print(f.read())
f.close()