import re


def validate_student_id(student_id):
    if not student_id.strip():
        raise ValueError("Student ID cannot be empty.")

    return student_id.strip()

def validate_name(name):
    name = name.strip()

    if not name:
        raise ValueError("Name cannot be empty.")

    if not name.replace(" ","").isalpha():
        raise ValueError("Name must contain only letters.")

    return name

def validate_age(age):
    try:
        age = int(age)
    except ValueError:
        raise ValueError("Age must be a number.")

    if age < 1 or age > 100:
        raise ValueError("Age must be between 1 and 100.")

    return age

def validate_email(email):
    email = email.strip()

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(pattern, email):
        raise ValueError("Please enter a valid email address.")
    
    return email

def validate_course(course):
    course = course.strip()

    if not course:
        raise ValueError("Course cannot be empty.")

    return course