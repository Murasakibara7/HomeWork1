class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def get_marks(self, lecturer, courses, grades):
        if isinstance(lecturer,
                      Lecturer) and courses in self.courses_in_progress and courses in lecturer.courses_attached:
            if courses in lecturer.grades:
                lecturer.grades[courses] += [grades]
            else:
                lecturer.grades[courses] = [grades]
        else:
            return 'Ошибка'

    def _st_average_grade(self):
        dict_ = []
        for i in self.grades.values():
            dict_ += i
        sr = round(sum(dict_) / len(dict_), 2)
        return sr


    def __str__(self):
        return f' Имя:{self.name} \n Фамилия:{self.surname} \n Средняя оценка за домашние задания:{self._st_average_grade()} \n Курсы в процессе изучения:{self.courses_in_progress} \n Завершенные курсы:{self.finished_courses}'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self._st_average_grade() > other._st_average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progres = []

    def _lecturers_average_grade(self):
        dict_ = []
        for i in self.grades.values():
            dict_ += i
        sr = round(sum(dict_) / len(dict_), 2)
        return sr

    def __str__(self):
        return f' Имя:{self.name} \n Фамилия:{self.surname} \n Средняя оценка за лекции: {self._lecturers_average_grade()}'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._lecturers_average_grade() > other._lecturers_average_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f' Имя:{self.name} \n Фамилия:{self.surname}'



def _sr_marks(list_student, course):
    count_sr = []
    for i in list_student:
         count_sr += i.grades[course]
    print(sum(count_sr) / len(count_sr))



cool_reviewer = Reviewer('Bob', 'Marley')
cool_reviewer.courses_attached += ['Git']
cool_reviewer.courses_attached += ['Python']



cool_lecturer = Lecturer('Djon', 'Week')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']



top_lecturer = Lecturer('Archi', 'Kreg')
top_lecturer.courses_attached += ['Python']
top_lecturer.courses_attached += ['Git']



beautiful_student = Student('Kenny', 'Makkornik', 'boy')
beautiful_student.finished_courses += ['Введение в программирование']
beautiful_student.courses_in_progress += ['Git']
beautiful_student.courses_in_progress += ['Python']



best_student = Student('Ruoy', 'Eman', 'girl')
best_student.finished_courses += ['Введение в программирование']
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']



best_student.get_marks(cool_lecturer, 'Python', 7.3)
best_student.get_marks(cool_lecturer, 'Python', 6.5)
best_student.get_marks(cool_lecturer, 'Python', 5.9)
best_student.get_marks(cool_lecturer, 'Python', 3.4)



best_student.get_marks(cool_lecturer, 'Git', 9.9)
best_student.get_marks(cool_lecturer, 'Git', 8.3)
best_student.get_marks(cool_lecturer, 'Git', 5.9)
best_student.get_marks(cool_lecturer, 'Git', 5.4)



beautiful_student.get_marks(top_lecturer, 'Git', 9.5)
beautiful_student.get_marks(top_lecturer, 'Git', 5.5)
beautiful_student.get_marks(top_lecturer, 'Git', 7.3)
beautiful_student.get_marks(top_lecturer, 'Git', 4.2)



beautiful_student.get_marks(top_lecturer, 'Python', 3.9)
beautiful_student.get_marks(top_lecturer, 'Python', 6.5)
beautiful_student.get_marks(top_lecturer, 'Python', 8.6)
beautiful_student.get_marks(top_lecturer, 'Python', 3.1)



cool_reviewer.rate_hw(best_student, 'Git', 1.4)
cool_reviewer.rate_hw(best_student, 'Git', 8.2)
cool_reviewer.rate_hw(best_student, 'Git', 7.1)
cool_reviewer.rate_hw(best_student, 'Git', 6.4)



cool_reviewer.rate_hw(best_student, 'Python', 7.1)
cool_reviewer.rate_hw(best_student, 'Python', 3.2)
cool_reviewer.rate_hw(best_student, 'Python', 6.4)
cool_reviewer.rate_hw(best_student, 'Python', 8.6)



cool_reviewer.rate_hw(beautiful_student, 'Python', 8.4)
cool_reviewer.rate_hw(beautiful_student, 'Python', 3.4)
cool_reviewer.rate_hw(beautiful_student, 'Python', 6.4)
cool_reviewer.rate_hw(beautiful_student, 'Python', 1.4)



cool_reviewer.rate_hw(beautiful_student, 'Git', 7.4)
cool_reviewer.rate_hw(beautiful_student, 'Git', 6.3)
cool_reviewer.rate_hw(beautiful_student, 'Git', 4.1)
cool_reviewer.rate_hw(beautiful_student, 'Git', 2.7)



print(best_student)
print()
print(beautiful_student)
print()
print(cool_lecturer)
print()
print(top_lecturer)
print()
print(cool_reviewer)
print()
print(cool_lecturer.__lt__(top_lecturer))
print()
print(best_student.__lt__(beautiful_student))
_sr_marks([best_student, beautiful_student], 'Git')
_sr_marks([best_student, beautiful_student], 'Python')
_sr_marks([cool_lecturer, top_lecturer], 'Git')
_sr_marks([cool_lecturer, top_lecturer], 'Python')