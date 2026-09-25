class Student:
    def __init__(self, student_id, name, age, email, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.course = course

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "course": self.course
        }

    @classmethod
    def from_dict(cls,data):
        return cls(
            data["student_id"],
            data["name"],
            data["age"],
            data["email"],
            data["course"]
        )

    def display(self):
        print("-" * 50)
        print(f"Student ID : {self.student_id}")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Email : {self.email}")
        print(f"Course : {self.course}")
        print("-" * 50)