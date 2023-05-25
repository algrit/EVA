from datetime import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

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


# def course_sub(request):
#     form = CourseSubscribeForm()
#     if request.method == 'POST':
#         try:
#             CourseSubscription.objects.get(
#                 Q(user_id=request.POST['user']) &
#                 Q(course_id=request.POST['course']) &
#                 Q(active=True))
#         except ObjectDoesNotExist:
#             pass
#         else:
#             request.POST['user'] = 123
#         new_sub = CourseSubscription(
#             user=User.objects.get(id=request.POST['user']),
#             course=Course.objects.get(id=request.POST['course'])
#         )
#         new_sub.save()
#         return HttpResponseRedirect('course_sub/done')
#     return render(request, 'education/course_sub_form.html', context={'form': form})

class CourseSub(CreateView):
    model = CourseSubscription
    form_class = CourseSubscribeForm
    template_name = 'education/course_sub_form.html'
    success_url = 'study_management'


class StudyManagement(ListView):
    model = CourseSubscription
    template_name = 'education/study_management.html'
    context_object_name = 'subs'
    ordering = ['-sub_time']
    paginate_by = 10


    def get_queryset(self):
        filter_val = self.request.GET.get('user_filter', 'all_users')
        try:
            searched_user = User.objects.get(username=filter_val)
        except ObjectDoesNotExist:
            return super().get_queryset()
        new_context = CourseSubscription.objects.filter(user=searched_user).order_by(F('sub_time').desc())
        return new_context

    def get_context_data(self, **kwargs):
        context = super(StudyManagement, self).get_context_data(**kwargs)
        context['user_filter'] = self.request.GET.get('user_filter', 'all_users')
        if context['user_filter'] == 'all_users':
            return context
        try:
            User.objects.get(username=self.request.GET['user_filter'])
        except ObjectDoesNotExist:
            context['message'] = 'No such User'
        return context


def course_unsub(request, pk: int):
    sub = CourseSubscription.objects.get(id=pk)
    if request.method == 'POST':
        sub.active = False
        sub.unsub_time = str(datetime.now()) + '+00:00'
        sub.save()
        return HttpResponseRedirect('/study_management')
    return render(request, 'education/course_unsub_form.html', {'sub': sub})
