from django.urls import path
from . import views

urlpatterns = [
    path('my', views.main_page)
]