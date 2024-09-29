def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif 80 <= percentage < 90:
        return 'B'
    elif 70 <= percentage < 80:
        return 'C'
    elif 60 <= percentage < 70:
        return 'D'
    else:
        return 'F'

# Input marks for 5 subjects
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))
subject4 = float(input("Enter marks for Subject 4: "))
subject5 = float(input("Enter marks for Subject 5: "))

# Calculate total marks
total_marks = subject1 + subject2 + subject3 + subject4 + subject5

# Calculate percentage
percentage = (total_marks / 500) * 100

# Calculate grade
grade = calculate_grade(percentage)

# Print total marks, percentage, and grade
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)