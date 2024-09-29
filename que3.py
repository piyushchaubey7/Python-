def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=' ')
        print() 

rows = 5

# Call the function to print the pattern
print_pattern(rows)

