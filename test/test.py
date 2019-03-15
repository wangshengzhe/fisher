# -*- coding: utf-8 -*-
class Human():
    sum = 0

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_name(self):
        print(self.name)


class Student(Human):
    def __init__(self, school, name, age):
        super(Student, self).__init__(name, age)
        self.school = school

    def do_homework(self):
        print("do homework")

    def out_school(self):
        print(self.school)


student1 = Student("北小", "tom", 15)
# student1.get_name()
student1.out_school()
student1.get_name()


a = '2    3f'
print(len(a))
