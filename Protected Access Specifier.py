class Student:
    
    def __init__(self, name, roll_number):
        self._name = name        
        self._roll_number = roll_number

    def _display_protected(self): # protected method (by convention)
        print(f"Protected info: {self._name}, {self._roll_number}")

class GraduateStudent(Student):
    
    def __init__(self, name, roll_number, research_topic):
        super().__init__(name, roll_number)
        self.research_topic = research_topic

    def display_details(self):
        print(f"Name: {self._name}") 
        print(f"Roll No: {self._roll_number}")
        print(f"Topic: {self.research_topic}")

grad_student = GraduateStudent("Yokesh", "21144050", "AI in cars")

print(grad_student._roll_number) 
grad_student._display_protected()  
grad_student.display_details()

Output:
21144050
Protected info: Yokesh, 21144050
Name: Yokesh
Roll No: 21144050
Topic: AI in cars