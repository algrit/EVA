from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()
router.register('api/questions', views.QuestionListView)


urlpatterns = [
    path('my', views.main_page),
    path('courses', views.courses)
]


urlpatterns += router.urls