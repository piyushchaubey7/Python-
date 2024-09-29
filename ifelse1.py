print("Enter the choice:")
choice = 0

    print("Press 1 for add record")
    print("Press 2 for delete record")
    print("Press 3 for update record")
    print("Press 4 for display record")
    print("Press 5 to exit application")
    
while choice != 5:
    choice = choice + 1


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
        print("User quits the application")
    else:
        print("Invalid choice")

exit(0)
