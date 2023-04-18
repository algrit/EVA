from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Question
from .serializers import QuestionSerializer


class QuestionListView(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


def main_page(request):
    return render(request, 'education/main_page.html')

def courses(request):
    return render(request, 'education/courses.html')
