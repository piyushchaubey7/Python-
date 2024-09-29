# Function to calculate grade based on percentage
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
marks = []
for i in range(5):
    while True:
        mark = float(input(f"Enter marks for Subject {i+1}: "))
        if 0 <= mark <= 100:
            marks.append(mark)
            break
        else:
            print("Invalid marks! Please enter marks between 0 and 100.")

# Calculate total marks
total_marks = sum(marks)

# Calculate percentage
percentage = (total_marks / (5 * 100)) * 100

# Calculate grade
grade = calculate_grade(percentage)

# Print total marks, percentage, and grade
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)