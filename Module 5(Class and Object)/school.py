class Student:
    def __init__(self, name, cur_class, id):
        self.name = name
        self.cur_class = cur_class
        self.id = id
    #class representation
    def __repr__(self):
        return f"Student with name: {self.name}, class: {self.cur_class}, ID: {self.id}"
class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self):
        return f"Teacher: {self.name}, Subject: {self.subject}"

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []
    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)
    def enroll(self, name, fee):
        if fee < 6500:
            return "Not Enough Fee"
        else:
            id = len(self.students) + 1
            student =  Student(name, 'C', id)
            self.students.append(student)
            return f"{name} is enrolled with id: {id}, extra money {fee - 6500}"
    def __repr__(self) -> str:
        print("Welcome to", self.name)
        print("-------------Our Teachers--------------------")
        for teacher in self.teachers:
            print(teacher)
        print("-------------Our Students---------------------")
        for student in self.students:
            print(student)
        return "Done for now"
         
# alia = Student("Alia Bhat", 8, 1)
# ranbeer = Teacher("Couran beer", "Algorithm", 101)
# print(alia)
# print(ranbeer)

phitron = School("Phitron")
phitron.enroll("Alia", 5200)
phitron.enroll("Rani", 8000)
phitron.enroll("Nily", 7000)
phitron.enroll("Vaijan", 90000)

phitron.add_teacher("Tom Cruise", "Algo")
phitron.add_teacher("Decap", "DS")
phitron.add_teacher("AJ", "Database")

print(phitron)

