def calculate_net_salary(rank, basic_salary):
    hra_percentage, da_percentage, pf_percentage = 0, 0, 0

    if rank == 1:
        hra_percentage = 0.09
        da_percentage = 0.10
        pf_percentage = 0.12
    elif rank == 2:
        hra_percentage = 0.07
        da_percentage = 0.40
        pf_percentage = 0.12
    elif rank == 3:
        hra_percentage = 0.05
        da_percentage = 0.30
        pf_percentage = 0.12
    else:
        print("Invalid rank entered!")
        return None

    hra = basic_salary * hra_percentage
    da = basic_salary * da_percentage
    pf = basic_salary * pf_percentage

    net_salary = basic_salary + hra + da - pf
    return net_salary

def main():
    rank = int(input("Enter rank of the employee (1, 2, or 3): "))
    basic_salary = float(input("Enter basic salary of the employee: "))

    net_salary = calculate_net_salary(rank, basic_salary)
    if net_salary is not None:
        print(f"Net Salary: ${net_salary:.2f}")

if __name__ == "__main__":
    main()
