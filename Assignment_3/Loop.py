choice = ""

while choice != "3":
    print()
    print("Menu:")
    print("1. Count from 1 to 25")
    print("2. Count from 25 to 1")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("Counting from 1 to 25:")
        for number in range(1, 26):  # Loop through numbers from 1 to 25
            print(number)  # Print the current number in the loop
        print("Counting complete!")  # Indicate that counting is finished
    elif choice == "2":
        print("Counting from 25 to 1:")
        for number in range(25, 0, -1):  # Loop through numbers from 25 to 1
            print(number)  # Print the current number in the loop
        print("Counting complete!")  # Indicate that counting is finished
    elif choice == "3":
        print("Exiting...")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")