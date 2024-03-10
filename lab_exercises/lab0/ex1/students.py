import math
import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"


class Subject:
    def __init__(self, name_of_subject='none', points_theory=0, points_practical=0, points_labs=0):
        self.name_of_subject = name_of_subject
        self.points_theory = points_theory
        self.points_practical = points_practical
        self.points_labs = points_labs

    def grade(self):
        grade_from_points = math.ceil((self.points_theory + self.points_labs + self.points_practical) / 10)
        if grade_from_points < 5:
            grade_from_points = 5
        return grade_from_points

    def __repr__(self):
        return f"----{self.name_of_subject}: {self.grade()}"


class Student:
    def __init__(self, name='none', surname='none', index='none'):
        self.name = name
        self.surname = surname
        self.index = index
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def __repr__(self):
        to_string = f"Student: {self.name} {self.surname}\n"
        for subject in self.subjects:
            to_string += str(subject) + "\n"

        return to_string


if __name__ == '__main__':
    students_dict = {}

    while True:
        user_input = input()
        if user_input == "end":
            break
        line = user_input.split(",")
        std_name = line[0]
        std_surname = line[1]
        std_index = line[2]
        sbj_name = line[3]
        sbj_theory = int(line[4])
        sbj_practical = int(line[5])
        sbj_labs = int(line[6])

        new_subject = Subject(sbj_name, sbj_theory, sbj_practical, sbj_labs)

        if std_index not in students_dict:
            new_student = Student(std_name, std_surname, std_index)
            students_dict[std_index] = new_student
        students_dict[std_index].add_subject(new_subject)

    for key in students_dict:
        print(students_dict[key])
