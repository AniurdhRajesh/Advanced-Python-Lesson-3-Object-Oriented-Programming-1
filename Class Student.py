class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"{self.name} has a grade of {self.grade}.")

student1 = Student("Alice", "A")
student1.display()
