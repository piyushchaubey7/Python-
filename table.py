print("============================Table Program===============================")

n = int(input("How many times do you want to find the table? "))

for i in range(1, n + 1):
    n1 = int(input(f"Enter the table number {i}: "))
    for j in range(1, 11):
        t = n1 * j
        print(f"{n1} * {j} = {t}")
