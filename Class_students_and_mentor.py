class Student:
    Summary_Students = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.Summary_Students.append(self)
        
    def average(self):
        return [sum(self.grades[f'{i}']) for i in self.grades][0] / [len(self.grades[f'{i}']) for i in self.grades][0]

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return (f'Имя: {self.name} \
        \nФамилия: {self.surname} \
        \nСредняя оценка за домашние задания: {self.average()} \
        \nКурсы в процессе изучения: {self.courses_in_progress} \
        \nЗавершенные курсы: {self.finished_courses}')

    def __lt__(self ,other):
        if not isinstance(other , Lecturer):          
            print("Other is a not Lecturer" )
            return
        return self.average() < other.average()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    Summary_Lecturer = []
    def __init__(self,name, surname):
        super().__init__(name,surname)
        self.grades = {}
        Lecturer.Summary_Lecturer.append(self)
    
    def average(self):
        return [sum(self.grades[f'{i}']) for i in self.grades][0] / [len(self.grades[f'{i}']) for i in self.grades][0]

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекцию: {self.average()}'

    def __lt__(self ,other):
        if not isinstance(other , Student):          
            print("Other is a not Student" )
            return
        return self.average() < other.average()
         
class Reviewer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name,surname)

    def __str__(self) -> str:
        return f'Имя: {self.name} \nФамилия: {self.surname}'
 
best_student_1 = Student('Ruoy', 'Eman', 'your_gender')
best_student_1.courses_in_progress += ['Python']

best_student_2 = Student('Vasya', 'Ivanov', 'male')
best_student_2.courses_in_progress += ['JS']

best_student_3 = Student('Vasya', 'Ivanov', 'male')
best_student_3.courses_in_progress += ['Python']

cool_mentor_1 = Mentor('Some', 'Buddy')
cool_mentor_1.courses_attached += ['Python']
cool_mentor_1.rate_hw(best_student_1, 'Python', 10)
cool_mentor_1.rate_hw(best_student_1, 'Python', 10)
cool_mentor_1.rate_hw(best_student_1, 'Python', 10)

cool_mentor_2 = Mentor('Jordj', 'Vurih')
cool_mentor_2.courses_attached += ['JS']
cool_mentor_2.rate_hw(best_student_2, 'JS', 7)
cool_mentor_2.rate_hw(best_student_2, 'JS', 3)
cool_mentor_2.rate_hw(best_student_2, 'JS', 5)

cool_mentor_1 = Mentor('Some', 'Buddy')
cool_mentor_1.courses_attached += ['Python']
cool_mentor_1.rate_hw(best_student_3, 'Python', 3)
cool_mentor_1.rate_hw(best_student_3, 'Python', 2)
cool_mentor_1.rate_hw(best_student_3, 'Python', 7)

Lecturer_1 = Lecturer("Trus", "Ubegai")
Lecturer_1.courses_attached += ['Python']
best_student_1.rate_hw(Lecturer_1, 'Python', 3)
best_student_1.rate_hw(Lecturer_1, 'Python', 6)
best_student_1.rate_hw(Lecturer_1, 'Python', 6)

Lecturer_2 = Lecturer("Fred", "Dib")
Lecturer_2.courses_attached += ['JS']
best_student_2.rate_hw(Lecturer_2, 'JS', 9)
best_student_2.rate_hw(Lecturer_2, 'JS', 8)
best_student_2.rate_hw(Lecturer_2, 'JS', 9)

Reviewer_1 = Reviewer("Brus", "Vsemog")

Summary_Course = ['JS']

print(best_student_1)
print(Lecturer_1)
print(Lecturer_1 < best_student_1)
print(best_student_2)
print(Reviewer_1)

def average_students(students : list,Summary_Course):
    sum_ = 0
    for st in Student.Summary_Students:
        if st.courses_in_progress == Summary_Course:
            sum_ += st.average()
    return sum_

print(f'Средняя ценка {average_students(Student.Summary_Students,Summary_Course)} за домашние задания по всем студентам в рамках конкретного курса {Summary_Course}')

def average_lecturer(lecturers : list,Summary_Course):
    sum_ = 0
    for lec in Lecturer.Summary_Lecturer:
        if lec.courses_attached == Summary_Course:
            sum_ += lec.average()
    return sum_

print(f'Средняя ценка {average_lecturer(Lecturer.Summary_Lecturer,Summary_Course)} за лекции всех лекторов в рамках курса {Summary_Course}')


