import os
import pickle


class Student:
    student_number = 1400

    def __init__(self):
        self.stu_fname = input('name :')
        self.stu_lname = input('family :')
        self.stu_id = Student.generator_stu_num()

    @classmethod
    def generator_stu_num(cls):
        cls.student_number += 1
        return cls.student_number


class Course:
    def __init__(self):
        self.course = input('enter name of course :')
        self.unit = input(' enter unit of course :')


class Grade:
    def __init__(self):
        self.id = int(input('student id :'))
        self.grade = int(input('enter grade :'))
        self.course = input('enter course :')


class Database:
    def __init__(self):
        if os.path.isfile('Database.pkl'):
            with open('Database.pkl', 'rb') as reader:
                self.dict = pickle.load(reader)
        else:
            self.dict = {}
            with open("Database.pkl", 'wb') as writer:
                pickle.dump(self.dict, writer)

    def add_student(self, stu):
        student = {
            "First name": stu.stu_fname,
            "Last name": stu.stu_lname,
            "Grades": []
        }
        self.dict.update({stu.stu_id: student})
        with open("Database.pkl", 'wb') as writer:
            pickle.dump(self.dict, writer)

    def add_grade(self, gra):
        self.dict[gra.id]['Grades'].append(gra.grade)
        with open("Database.pkl", 'wb') as writer:
            pickle.dump(self.dict, writer)

    def add_course(self, cour):
        course = {
            cour.course: cour.unit
        }
        self.dict.update({"Courses": course})
        with open("Database.pkl", 'wb') as writer:
            pickle.dump(self.dict, writer)

    def get_all_student(self):
        studentlist = []
        for key, value in self.dict.items():
            studentlist.append(value['First name'])
        return studentlist

    def get_average_grades(self, stu):
        student = stu.stu_id
        student_grades = self.dict[student]['Grades']
        return sum(student_grades) / len(student_grades)


a = Student()
a1 = Student()
a3 = Student()
b = Database()
b.add_student(a)
b.add_student(a1)
b.add_student(a3)

g = Grade()
g1 = Grade()
g2 = Grade()

b.add_grade(g)
b.add_grade(g1)
b.add_grade(g2)

print(b.dict)
print(b.get_all_student())
print(b.get_average_grades(a))
