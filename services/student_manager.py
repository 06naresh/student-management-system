from models.student import Student
from utils.file_handler import FileHandler

class StudentManager:
    def __init__(self, file_path):
         self.file_handler = FileHandler(file_path)
         self.student = []
         self.load_students()

    def load_students(self):
         data = self.file_handler.read_data()

         self.students = [
              Student.from_dict(student_data)
              for student_data in data
         ]

    def save_students(self):
         data = [
              student.to_dict()
              for student in self.students
         ]

         return self.file_handler.write_data(data)

    def add_student(self,student):
         if self.find_student(student.student_id):
              raise ValueError(f"Student ID '{student.student_id}' already exists.")

         self.students.append(student)

         if self.save_students():
              return True

         self.students.pop()
         return False

    def get_all_students(self):
         return self.students

    def find_student(self,student_id):
        for student in self.students:
              if student.student_id.lower() == student_id.lower():
                   return student
        return None

    def search_students(self,keyword):
         keyword = keyword.lower()

         return [
              student 
              for student in self.students
              if keyword in student.student_id.lower()
              or keyword in student.name.lower()
              or keyword in student.course.lower()
         ]

    def update_student(self, student_id, name=None, age=None, email=None, course=None):
         student = self.find_student(student_id)

         if student is None:
              return False

         if name is not None:
              student.name = name

         if age is not None:
              student.age = age

         if email is not None:
              student.email = email

         if course is not None:
              student.course = course

         return self.save_students()

    def delete_students(self, student_id):
         student = self.find_student(student_id)

         if student is None:
              return False
         
         self.students.remove(student)

         if self.save_students():
              return True
         
         self.students.append(student)
         return False