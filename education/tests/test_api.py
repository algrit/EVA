from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse

from education.models import Test, Course
from education.serializers import CourseSerializer


class CoursesApiTestCase(APITestCase):
    def test_get(self):
        test_course1 = Course.objects.create(title='test_course1')
        test_course2 = Course.objects.create(title='test_course2')
        url = reverse('course-list')
        print(url)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        serializer_data = CourseSerializer([test_course1, test_course2], many=True).data
        self.assertEqual(serializer_data, response.data)
        print(serializer_data)
        print(response.data)
