from django.shortcuts import render
from django.views.generic import ListView, DetailView

from education.models import Course, Test


def main_page(request):
    return render(request, 'education/main_page.html', {'courses': Course.objects.all()})

class TestsListView(ListView):
    model = Test
    template_name = 'education/tests_list.html'

class TestDetailView(DetailView):
    model = Test
    template_name = 'education/test_detail.html'




class CoursesListView(ListView):
    model = Course
    template_name = 'education/courses_list.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'education/course_detail.html'
