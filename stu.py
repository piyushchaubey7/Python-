def calculate_percentage(total_marks, total_subjects):
    return (total_marks / (total_subjects * 100)) * 100

def calculate_division(percentage):
    if percentage >= 60:
        return "First division"
    elif 50 <= percentage <= 59:
        return "Second division"
    elif 40 <= percentage <= 49:
        return "Third division"
    else:
        return "Fail"

def main():
    total_subjects = 5
    total_marks = 0

    for i in range(total_subjects):
        marks = int(input(f"Enter marks obtained in subject {i+1}: "))
        total_marks += marks

    percentage = calculate_percentage(total_marks, total_subjects)
    division = calculate_division(percentage)

    print(f"Percentage: {percentage}%")
    print(f"Division: {division}")

if __name__ == "__main__":
    main()
