l=["piyush\n","pawan\n","shivam\n","naveen\n"]


f=open("abc.txt","a")

f.writelines(l)
f.write("student")
print("list data written in file");

f.close();