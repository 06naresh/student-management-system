from models.student import Student
from services.student_manager import StudentManager
from utils.validators import validate_student_id, validate_age, validate_course, validate_name, validate_email


DATA_FILE = "data/students.json"

student_manager = StudentManager(DATA_FILE)

def print_header():
    print("\n" + "=" *50)
    print("          STUDENT MANAGEMENT SYSTEM")
    print("=" *50)

def display_menu():
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def add_student():
    print("\n--- Add Student ---")

    try:
        student_id = validate_student_id(input("Enter student ID: "))

        name = validate_name(input("Enter name: "))

        age = validate_age(input("Enter age:"))

        email = validate_email(input("Enter email: "))

        course = validate_course(input("Enter course: "))


        student = Student(student_id,name,age,email,course)

        if student_manager.add_student(student):
            print("\nStudent added successfully.")
        else:
            print("\nFailed to save student.")

    except ValueError as err:
        print(f"\nError: {err}")


def view_students():
    print("\n--- All Students ---")

    students = student_manager.get_all_students()

    if not students:
        print("No students found.")
        return

    print(f"\nTotal Students: {len(students)}")

    for student in students:
        student.display()

def search_student():
    print("\n--- Search Student ---")

    keyword = input("Enter student ID, name, or course: ").strip()

    if not keyword:
        print("Search value cannot be empty.")
        return

    students = student_manager.search_students(keyword)

    if not students:
        print("No matching students found.")
        return

    print(f"\nFound {len(students)} student(s).")

    for student in students:
        student.display()

def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter student ID to update: ").strip()

    student = student_manager.find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    print("\nLeave a field empty to keep the current value.")

    try:
        name_input = input(f"Name [{student.name}]").strip()

        age_input = input(f"Age [{student.age}]").strip()

        email_input = input(f"Email [{student.email}]").strip()

        course_input = input(f"Course [{student.course}]").strip()

        name = (
            validate_name(name_input)
            if name_input
            else None
            )
        
        age = (
            validate_age(age_input)
            if age_input
            else None
        )

        email = (
            validate_email(email_input)
            if email_input
            else None
        )

        course = (
            validate_course(course_input)
            if course_input
            else None
        )

        if student_manager.update_student(student_id,name, age,email,course):
            print("\nStudent update successfully.")

        else:
            print("\nFailed to update student.")

    except ValueError as err:
        print(f"\nError: {err}")


def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter student ID to delete: ")

    student = student_manager.find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    student.display()

    confirmation = input("Are you sure you want to delete this student? (y/n): ").strip().lower()

    if confirmation != "y":
        print("Delete operation cancelled.")
        return
    if student_manager.delete_students(student_id):
        print("\nStudent deleted successfully.")

    else:
        print("\nFailed to delete student.")


def main():
    while True:
        print_header()
        display_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("\nThank you for using Student Management System.")
            break
        else:
            print("\nInvalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()