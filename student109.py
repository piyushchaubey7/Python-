
rollno=int(input("Enter the rollno:- "));
name=input("Enter the name:- ")

print("Enter the 5 subject marks:- ")

hindi=int(input("Enter hindi marks:- "));
if 0 <= hindi and hindi <= 100: 
      print(hindi);  
else:
       print("Invalid marks! Please enter marks between 0 and 100.")
english=int(input("Enter english marks:- "));
if 0 <= english and english <= 100:  
       print(english) 
else:
       print("Invalid marks! Please enter marks between 0 and 100.")
science=int(input("Enter science marks:- "));
if 0 <= science and science <= 100: 
     print(science)    
else:
    print("Invalid marks! Please enter marks between 0 and 100.") 
social=int(input("Enter social science marks:- "));
if 0 <= socail and socail <= 100:  
   print(socail)  
else:
   print("Invalid marks! Please enter marks between 0 and 100.")
math=int(input("Enter math marks:- "));
if 0 <= math and math <= 100:
   print(math)
else:
    print("Invalid marks! Please enter marks between 0 and 100.")


# Calculate total marks
total=hindi+english+science+social+math
print("======================================================================================")
print("total marks = ",total)
print("======================================================================================")
percentage=total/5;
print("percentage=  ",percentage,"%")


if(percentage>=90):
         print("A")
    elif 80 <= percentage and percentage < 90:
        print("B")
    elif 70 <= percentage and percentage < 80:
        print("C")
    elif 60 <= percentage and percentage< 70:
        print("D")
    else:
        print("Fail")