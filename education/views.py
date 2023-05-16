from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from education.forms import CourseSubscribeForm
from education.models import Course, Test, CourseSubscription

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


def course_sub(request):
    form = CourseSubscribeForm()
    if request.method == 'POST':
        try:
            CourseSubscription.objects.get(Q(user_id=request.POST['user']) & Q(course_id=request.POST['course'])
                                          & Q(active=True))
        except ObjectDoesNotExist:
            pass
        else:
            request.POST['user'] = 123
        new_sub = CourseSubscription(
            user=User.objects.get(id=request.POST['user']),
            course=Course.objects.get(id=request.POST['course'])
        )
        new_sub.save()
        return HttpResponseRedirect('course_sub/done')
    return render(request, 'education/course_sub_form.html', context={'form': form})


def sub_done(request):
    return render(request, 'education/sub_done.html')