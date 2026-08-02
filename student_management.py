class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("\n-----------------------")
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("-----------------------")


# Initial Students
students = {
    101: Student(101, "Mehtab", 20, "Python"),
    102: Student(102, "Mashal", 19, "SQL")
}

while True:
    print("\n======= Student Management System =======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Students")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid menu number.")
        continue

    # Add Student
    if choice == 1:
        student_id = int(input("Enter Student ID: "))

        if student_id in students:
            print("Student ID already exists.")
        else:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")

            students[student_id] = Student(student_id, name, age, course)
            print("Student added successfully!")

    # View Students
    elif choice == 2:
        if len(students) == 0:
            print("No students found.")
        else:
            for stu in students.values():
                stu.display()

    # Search Student
    elif choice == 3:
        student_id = int(input("Enter Student ID: "))

        if student_id in students:
            students[student_id].display()
        else:
            print("Student not found.")

    # Update Student
    elif choice == 4:
        student_id = int(input("Enter Student ID to Update: "))

        if student_id in students:
            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            course = input("Enter New Course: ")

            students[student_id].name = name
            students[student_id].age = age
            students[student_id].course = course

            print("Student Updated Successfully!")
        else:
            print("Student not found.")

    # Delete Student
    elif choice == 5:
        student_id = int(input("Enter Student ID to Delete: "))

        if student_id in students:
            del students[student_id]
            print("Student Deleted Successfully!")
        else:
            print("Student not found.")

   #Total Students
    elif choice == 6:
        print("\nTotal Students: ",len(students))
        break

    # Invalid Choice
    else:
        print("Invalid choice.")