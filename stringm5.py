u=i=d=s=sp=0

str=input("Enter string")
for x in str:
  if x.isupper():
     u+=1
   elif x.islower():
     i+=1
   elif x.isdigit():
      d+=1
   elif x.isspace():
     s+=1
   else:
    sp+1
print("total upper letter=",u)
print("total lower letter=",i)
print("total special  letter=",sp)
print("total  space=",s)
print("total digit=",d)

