from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Question, Test, Course
from .serializers import QuestionSerializer, CourseSerializer, TestSerializer


class QuestionListView(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class TestListView(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class CourseListView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


def main_page(request):
    return render(request, 'education/main_page.html')


def question(request):
    return render(request, 'education/questions.html')


def test(request):
    return render(request, 'education/tests.html')


def course(request):
    return render(request, 'education/courses.html')
