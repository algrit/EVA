from unittest.case import TestCase

from education.models import Course
from education.serializers import CourseSerializer


class CourseSerializerTestCase(TestCase):
    def test_ok(self):
        test_course1 = Course.objects.create(title='test_course1')
        test_course2 = Course.objects.create(title='test_course2')
        data = CourseSerializer([test_course1, test_course2], many=True).data
        expected_data = [
            {
                'id': test_course1.id,
                'title': 'test_course1',
                'tests': []
            },
            {
                'id': test_course2.id,
                'title': 'test_course2',
                'tests': []
            }
        ]
        self.assertEqual(data, expected_data)
