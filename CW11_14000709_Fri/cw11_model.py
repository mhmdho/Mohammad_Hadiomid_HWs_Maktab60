# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 16:37:30 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 11 - Model    (1400-07-09 - Friday - part 2)
# =============================================================================

import redis
redis_client = redis.Redis()


class Student:
    ''' Student information class '''

    def __init__(self, name, age):
        student_number = redis_client.get('student_number').decode('utf-8')
        redis_client.incr('student_number')
        self.student_number = student_number
        self.name = name
        self.age = age
        self.avg_grades = 0

    def save(self):
        ''' save to redis '''
        redis_client.hmset(
            f'student:{self.student_number}:info',
            {
                "name": self.name,
                "age": self.age,
                "student_number": self.student_number
            }
        )
        # print(redis_client.hmget(f'student:{self.student_number}:info','name'))

    def add_grade(self, grades):
        ''' Adding grade method '''
        redis_client.rpush(f'student:{self.student_number}:grades', *grades)
        return redis_client.lrange(f"student:{self.student_number}:grades",
                                   start=0, end=-1)

    def get_gpa(self):
        ''' Calculating GPA method '''
        grades = redis_client.lrange(f"student:{self.student_number}:grades",
                                     start=0, end=-1)
        gpa = 0
        for grade in grades:
            gpa += float(grade.decode('utf-8'))
            self.avg_grades = gpa/len(grades)
        return self.avg_grades

    def add_course(self, courses, term):
        ''' Adding course method '''
        cors = Course(courses, term)
        cors.save()
        cors.get_all_courses()
        cors.get_all_courses_by_term(term)

    @staticmethod
    def get_all_students():
        ''' Show all student '''
        return redis_client.keys(pattern="student:*:info")


class Course:
    """ student's course class """

    def __init__(self, name, term) -> None:
        self.course_id = redis_client.get('course_id').decode('utf-8')
        redis_client.incr('course_id')
        self.term = term
        self.name = name

    def save(self):
        ''' sade redis '''
        redis_client.hmset(
            f'course:{self.course_id}:info',
            {
                "name": self.name,
                "term": self.term,
                "course_id": self.course_id
            }
        )

    @staticmethod
    def get_all_courses():
        ''' show all courses of a student '''
        return redis_client.keys(pattern="course:*:info")

    @staticmethod
    def get_all_courses_by_term(term):
        ''' show all courses of a student in an entry term '''
        courses = redis_client.keys(pattern="course:*:info")
        for course in courses:
            test = redis_client.hmget(course.decode('utf-8'), keys='term')
            if f"b'{term}'" == str(test[0]):
                cs_term = redis_client.hmget(
                    course.decode('utf-8'), keys='name')
                return cs_term
            return f'No course found'
