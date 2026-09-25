# Student Management System

A terminal-based Student Management System developed using Python.

## GitHub Repository

You can find the source code for this project on GitHub:

**GitHub:** https://github.com/06naresh/student-management-system

---

## Features

* Add student
* View students
* Search student
* Update student
* Delete student
* JSON file storage
* Input validation
* Exception handling

---

## Project Structure

```text
student-management-system/
│
├── data/
│   └── students.json
│
├── models/
│   ├── __init__.py
│   └── student.py
│
├── services/
│   ├── __init__.py
│   └── student_manager.py
│
├── utils/
│   ├── __init__.py
│   ├── file_handler.py
│   └── validators.py
│
├── main.py
├── README.md
└── .gitignore
```

---

## Requirements

* Python 3.x
* VS Code or any Python-supported IDE
* Git (optional, for version control)

This project uses Python's built-in modules, so no external packages are required.

---

## How to Run

### 1. Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/06naresh/student-management-system.git
```


### 2. Open the Project

Open the project folder in VS Code:

```bash
cd student-management-system
```

### 3. Run the Application

Run the following command in the terminal:

```bash
python main.py
```

---

## Application Output

When you run the application, the main menu will be displayed:

```text
==================================================
          STUDENT MANAGEMENT SYSTEM
==================================================

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

Enter your choice:
```

---

## Example: Add Student

Select option `1` to add a student:

```text
Enter your choice: 1

--- Add Student ---

Enter student ID: S101
Enter name: Rahul
Enter age: 21
Enter email: rahul@gmail.com
Enter course: Python

Student added successfully.
```

The student information is stored in the JSON file:

```text
data/students.json
```

---

## Main Operations

### 1. Add Student

Adds a new student to the system.

The application collects:

* Student ID
* Name
* Age
* Email
* Course

Example:

```text
Student ID: S101
Name: Rahul
Age: 21
Email: rahul@gmail.com
Course: Python
```

---

### 2. View All Students

Displays all students currently stored in the system.

---

### 3. Search Student

Allows you to search for a student using the student ID.

Example:

```text
Enter student ID to search: S101
```

---

### 4. Update Student

Allows you to modify an existing student's information.

Example:

```text
Enter student ID to update: S101
```

You can update details such as:

* Name
* Age
* Email
* Course

---

### 5. Delete Student

Removes a student from the system using their student ID.

Example:

```text
Enter student ID to delete: S101
```

---

### 6. Exit

Closes the Student Management System.

---

## Data Storage

Student records are stored in a JSON file:

```text
data/students.json
```

Example:

```json
[
    {
        "student_id": "S101",
        "name": "Rahul",
        "age": 21,
        "email": "rahul@gmail.com",
        "course": "Python"
    }
]
```

JSON allows the application to preserve student information even after the program is closed.

---

## Exception Handling

The application uses exception handling to prevent the program from crashing when invalid input or file-related errors occur.

Examples include:

* Invalid age
* Invalid student ID
* Invalid email
* Student not found
* File not found
* Invalid JSON data
* Invalid menu choice

---

## Input Validation

The application validates user input before storing student information.

For example:

* Student ID should be provided.
* Name should not be empty.
* Age should be a valid number.
* Email should have a valid format.
* Course should not be empty.

---

## Object-Oriented Programming

The project uses a `Student` class to represent student information.

Each student is created as an object containing:

```text
Student ID
Name
Age
Email
Course
```

The project also separates responsibilities into different modules such as:

* `models` → Student class
* `services` → Student management operations
* `utils` → File handling and validation
* `main.py` → Application menu and program entry point

---

## Technologies Used

* Python
* JSON
* Object-Oriented Programming
* File Handling
* Exception Handling
* Git
* GitHub
* VS Code

---

## Author

**T Naresh**

GitHub: https://github.com/06naresh

---

## License

This project is created for learning and educational purposes.
