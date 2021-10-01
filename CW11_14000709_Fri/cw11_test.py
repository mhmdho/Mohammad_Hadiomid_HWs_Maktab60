# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 16:52:12 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 11 - Test of Model    (1400-07-09 - Friday - part 2)
# =============================================================================

import unittest
import redis
from model import Student, Course


class TestStudentMethods(unittest.TestCase):
    ''' Test student class to work correctly '''

    def setUp(self):
        ''' Define redis '''
        self.redis_client = redis.Redis()

    def test_save(self):
        ''' Test save '''
        student = Student('Ali', 20)
        student.save()

        student_from_redis = self.redis_client.hmget(
            f'student:{student.student_number}:info',
            'name')
        self.assertIsNotNone(student_from_redis)
        self.assertEqual(student_from_redis[0].decode('utf-8'), student.name)

    def test_student_number_incr(self):
        ''' Test student number'''
        student_number = self.redis_client.get(
            'student_number').decode('utf-8')

        student = Student('Ali', 20)
        student.save()
        student = Student('Mohammad', 25)
        student.save()

        new_student_number = self.redis_client.get(
            'student_number').decode('utf-8')

        self.assertEqual(int(new_student_number), int(student_number)+2)

    def test_add_grade(self):
        ''' test add grade method '''
        student = Student('Ali', 20)
        student.add_grade([20, 19])
        mylist = self.redis_client.lrange(
            name=f"student:{student.student_number}:grades", start=0, end=-1)
        lst = [x.decode('UTF8') for x in mylist]
        self.assertEqual(lst, ["20", "19"])

    def test_get_gpa(self):
        ''' Test get gpa method '''
        student = Student('Ali', 20)
        student.add_grade([20, 19])
        student.get_gpa()
        self.assertEqual(student.avg_grades, 19.5)


class TestCourseMethods(unittest.TestCase):
    ''' Test course class to work correctly '''

    def setUp(self):
        ''' Define redis '''
        self.redis_client = redis.Redis()

    def test_save(self):
        ''' Test save '''
        crs = Course('math', 1402)
        crs.save()
        cs_fromredis = self.redis_client.hmget(
            f'course:{crs.course_id}:info',
            'name')
        self.assertIsNotNone(cs_fromredis)
        self.assertEqual(cs_fromredis[0].decode('utf-8'), crs.name)

    def test_all_course(self):
        ''' Test all course method '''
        crs = Course('math', 1402)
        crs.save()
        all_cs = crs.get_all_courses()
        self.assertEqual(self.redis_client.keys(
            pattern="course:*:info"), all_cs)

    def test_all_courses_term(self):
        ''' Test courses in a term '''
        crs = Course('math', 1402)
        crs.save()
        term_cs = crs.get_all_courses_by_term(1402)
        self.assertIsNotNone(term_cs)


if __name__ == '__main__':
    unittest.main(verbosity=1)
