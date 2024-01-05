class Exam:
    exam_name = "Yearly Exam"
    def __init__(self, name):
        self.name = name
        self.subjects = []
    def add_subject(self, sub_name):
        self.subjects.append(sub_name)
    def show_subject(self):
        return self.subjects
        

niloy = Exam("Niloy")
niloy.add_subject("Biggan")
niloy.add_subject("Gonit")
niloy.add_subject("Biggan")

print(niloy.show_subject())

Nabid = Exam("Nabid")
Nabid.add_subject("Science")
Nabid.add_subject("Math")
Nabid.add_subject("Lae")

print(Nabid.show_subject())