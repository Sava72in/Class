class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self) -> str:
        for i in self.grades:
            sum_ = sum(self.grades[f'{i}'])
        average = sum_/(len(self.grades[f'{i}']))
        res = (f'Имя: {self.name} \
        \nФамилия: {self.surname} \
        \nСредняя оценка за домашние задания: {average} \
        \nКурсы в процессе изучения: {self.courses_in_progress} \
        \nЗавершенные курсы: {self.finished_courses}')
        return res
        
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
    def __init__(self,name, surname):
        super().__init__(name,surname)
        self.grades = {}
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average = [sum(self.grades[f'{i}']) for i in self.grades][0] / [len(self.grades[f'{i}']) for i in self.grades][0]
        res = (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекцию: {average}')
        return res 

    def __lt__(self ,other):
        self.average = [sum(self.grades[f'{i}']) for i in self.grades]
    

    def av(self):
        return [sum(self.grades[f'{i}']) for i in self.grades][0] / [len(self.grades[f'{i}']) for i in self.grades][0]
         



class Reviewer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name,surname)

    def __str__(self) -> str:
        res = (f'Имя: {self.name} \nФамилия: {self.surname}')
        return res
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

best_student = Student('Vasya', 'Ivanov', 'male')
best_student.courses_in_progress += ['JS'] + ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor = Mentor('Jordj', 'Vurih')
cool_mentor.courses_attached += ['JS']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'JS', 7)
cool_mentor.rate_hw(best_student, 'JS', 3)
cool_mentor.rate_hw(best_student, 'JS', 5)

Lecturer_ = Lecturer("Trus", "Ubegai")
Lecturer_.courses_attached += ['Python']
Lecturer_.rate_hw(best_student, 'Python', 3)
Lecturer_.rate_hw(best_student, 'Python', 6)
Lecturer_.rate_hw(best_student, 'Python', 6)

Lecturer_ = Lecturer("Fred", "Dib")
Lecturer_.courses_attached += ['JS']
Lecturer_.rate_hw(best_student, 'JS', 9)
Lecturer_.rate_hw(best_student, 'JS', 8)
Lecturer_.rate_hw(best_student, 'JS', 9)

Reviewer_ = Reviewer("Brus", "Vsemog")

print(Lecturer_)
# print(best_student)
# print(Reviewer_)
