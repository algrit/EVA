from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()
router.register('api/questions', views.QuestionListView)
router.register('api/tests', views.TestListView)
router.register('api/courses', views.CourseListView)


urlpatterns = [
    path('my', views.main_page),
    path('question', views.question),
    path('test', views.test),
    path('course', views.course)
]


urlpatterns += router.urls