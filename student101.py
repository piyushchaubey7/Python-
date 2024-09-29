rollno = int(input("Enter the roll number: "))
name = input("Enter the name: ")

print("Enter the 5 subject marks:- ")

if 0 <= hindi <= 100:
    hindi = int(input("Enter hindi marks: "))

english = int(input("Enter english marks: "))
elif 0 <= english <= 100:
    english = int(input("Enter english marks: "))

elif 0 <= science <= 100:
	science = int(input("Enter science marks: "))

    


elif 0 <= social <= 100:
	social = int(input("Enter social science marks: "))
    


elif 0 <= math <= 100:
	math = int(input("Enter math marks: "))
    
else:
    print("Invalid marks! Please enter marks between 0 and 100.")

# Calculate total marks
total = hindi + english + science + social + math
print("======================================================================================")
print("Total marks = ", total)
print("======================================================================================")
percentage = total / 5
print("Percentage = ", percentage, "%")

if percentage >= 90:
    print("Grade: A")
elif 80 <= percentage < 90:
    print("Grade: B")
elif 70 <= percentage < 80:
    print("Grade: C")
elif 60 <= percentage < 70:
    print("Grade: D")
else:
    print("Grade: Fail")
