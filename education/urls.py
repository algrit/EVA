from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views


# router = SimpleRouter()
# router.register('api/questions', views.QuestionListView)
# router.register('api/tests', views.TestListView)
# router.register('api/courses', views.CourseListView)


urlpatterns = [
    # path('', views.main_page),
    path('my', views.main_page),
    # path('question', views.question),
    path('test/<int:pk>', views.TestDetailView.as_view(), name='test_details'),
    path('test', views.TestsListView.as_view()),
    path('study_management', views.StudyManagement.as_view(), name='study_management'),
    path('course_sub', views.CourseSub.as_view()),
    path('course_unsub/<int:pk>', views.course_unsub, name='course_unsub'),
    path('course/<slug:slug>', views.CourseDetailView.as_view(), name='course_details'),
    path('course', views.CoursesListView.as_view())
]


# urlpatterns += router.urls