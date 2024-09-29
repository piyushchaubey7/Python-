
choice = 0

while choice != 5:
    print("Press 1 for add record")
    print("Press 2 for delete record")
    print("Press 3 for update record")
    print("Press 4 for display record")
    print("Press 5 to exit application")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Record added")
    elif choice == 2:
        print("Record deleted")
    elif choice == 3:
        print("Record updated")
    elif choice == 4:
        print("Record displayed")
    elif choice == 5:
        exit(0)
    else:
        print("Invalid choice")

