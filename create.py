from main import Student
a = Student()
while True:
    print("Welcome to student portal")
    print()
    print("1. Create table")
    print("2. Add student")
    print("3. Update student")
    print("4. Show student")
    print("5. Delete student")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            a.create_table()
        elif choice == 2:
            id = int(input("Enter student id: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            a.add_student(id, name, age)
        elif choice == 3:
            id = int(input("Enter student id: "))
            name = input("Enter student new name: ")
            age = int(input("Enter student new age: "))
            a.update_student(id, name, age)
        elif choice == 4:
            a.show_student()
        elif choice == 5:
            id = int(input("Enter student id: "))
            a.delete_student(id)
        elif choice == 6:
            print("Thank you for using student portal")
            break
        else:
            print("Invalid choice")
    except Exception as e:
        print("Error: ", e)


