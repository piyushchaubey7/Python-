def is_valid_triangle(A, B, C):
    
    if A + B + C == 180:
        return 1  # Valid triangle
    else:
        return 0  # Not a valid triangle

# Input angles
A = int(input("Enter the 1 angle"))
B = int(input("Enter the 2 angle"))
C = int(input("Enter the 3 angle"))
# if the triangle is valid
result = is_valid_triangle(A, B, C)
print(result)