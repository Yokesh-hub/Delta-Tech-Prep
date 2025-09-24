class Student:
    
    def __init__(self, name, roll_number):
        self.name = name          
        self.roll_number = roll_number 

    def display_info(self):  
        print(f"Name: {self.name}, Roll No: {self.roll_number}")

student1 = Student("Yokesh", "21144050")
print(student1.name)  
student1.display_info()  

Output:
Yokesh
Name: Yokesh, Roll No: 21144050
