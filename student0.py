print("=====================================Student Marksheet============================")





rollno=int(input("Enter the rollno:- "));
name=input("Enter the name:- ")
print("Enter the 5 subject marks:- ")

hindi=int(input("Enter hindi marks:- "));
english=int(input("Enter english marks:- "));
science=int(input("Enter science marks:- "));
social=int(input("Enter social science marks:- "));
math=int(input("Enter math marks:- "));
total=hindi+english+science+social+math
print("======================================================================================")
print("total marks = ",total)
print("======================================================================================")
percentage=total/5;
print("percentage=  ",percentage,"%")
if percentage >= 90:
     print("A");
           elif 80 <= percentage < 90:
        	  print("B")
                  elif 70 <= percentage < 80:
        	     print("C")
                   elif 60 <= percentage < 70:
       		      print("D")
        else:   
          print("Fail")
