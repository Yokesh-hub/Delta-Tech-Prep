
class Student:

    def __init__(self, name, roll_number):
        self.name = name 
        self.roll_number = roll_number
        self.grades = [] 
        
    def add_grade(self, grade):
        self.grades.append(grade)
    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades) 
    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_number}, Avg Grade: {self.get_average_grade():.2f}")

student_list = []  
student1 = Student("Ramesh", "8147")
student1.add_grade(85) 
student1.add_grade(90)
student1.add_grade(86)

student2 = Student("suresh", "8148")
student2.add_grade(78)
student2.add_grade(88)
student2.add_grade(96)

student_list.append(student1)
student_list.append(student2)
print("Student Information:")
for student in student_list:
    student.display_info()