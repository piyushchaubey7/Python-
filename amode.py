l=["piyush","pawan","shivam","naveen"]


f=open("abc.txt","a")

f.writelines(l)
f.write("student")
print("list data written in file");

f.close();