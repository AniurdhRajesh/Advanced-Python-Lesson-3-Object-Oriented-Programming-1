class Student:
    grade = "A"
    name = "Sam"

    def print_sentence(self):
        print("This is a student.")

    def print_class_variables(self):
        print(f"Name: {self.name}, Grade: {self.grade}")

student1 = Student()
student1.print_sentence()
student1.print_class_variables()
