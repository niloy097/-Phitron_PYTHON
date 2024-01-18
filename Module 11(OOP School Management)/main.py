from school import School, ClassRoom, Subject
from Persons import Student, Teacher
def main():
    
    school = School("Adam jee", "Uttara")
    
    eight = ClassRoom('eight')
    school.add_classroom(eight)
    
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    
    ten = ClassRoom('ten')
    school.add_classroom(ten)
    
    #add students
    abul = Student("Abul khan", eight)
    school.student_addmission(abul)
    babul = Student("Babul khan", eight)
    school.student_addmission(babul)
    cabul = Student("Cabul khan", eight)
    school.student_addmission(cabul)
    
    #subjects
    physics_teacher = Teacher("Sahjahan Tapan Rana")
    physics = Subject("Physics", physics_teacher)
    eight.add_subject(physics)
    
    chemistry_teacher = Teacher("Haradon Nag")
    chemistry = Subject("chemistry", chemistry_teacher)
    eight.add_subject(chemistry)
    
    biology_teacher = Teacher("Azmal Sir")
    biology = Subject("biology", biology_teacher)
    eight.add_subject(biology)
    
    eight.take_semester_final()
    print(school)
    
    

if __name__ == '__main__':
    main()