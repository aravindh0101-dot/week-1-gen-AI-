students = [
   {"name":"Aravindh","age":"20","course":"Gen AI"}
]

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":

        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = {
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)

        print("Student Added Successfully!")

    # View Students
    elif choice == "2":

        if len(students) == 0:
            print("No Students Found")

        else:
            print("\nStudent Records")

            for student in students:

                print("-------------------")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])

    # Search Student
    elif choice == "3":

        search_name = input("Enter Student Name to Search: ")

        found = False

        for student in students:

            if student["name"].lower() == search_name.lower():

                print("Student Found")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])

                found = True

        if not found:
            print("Student Not Found")

    # Update Student
    elif choice == "4":

        update_name = input("Enter Student Name to Update: ")

        found = False

        for student in students:

            if student["name"].lower() == update_name.lower():

                new_age = input("Enter New Age: ")
                new_course = input("Enter New Course: ")

                student["age"] = new_age
                student["course"] = new_course

                print("Student Updated Successfully")

                found = True

        if not found:
            print("Student Not Found")

    # Delete Student
    elif choice == "5":

        delete_name = input("Enter Student Name to Delete: ")

        found = False

        for student in students:

            if student["name"].lower() == delete_name.lower():

                students.remove(student)

                print("Student Deleted Successfully")

                found = True
                break

        if not found:
            print("Student Not Found")

    # Exit
    elif choice == "6":

        print("Thank You!")
        break

    else:
        print("Invalid Choice")