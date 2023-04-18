from django.contrib import admin

from education.models import Question, Test, Course


# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'question_text', 'correct_answer', 'incorrect_answer1', 'incorrect_answer2',
                    'comment']
    fields = ['question_text', 'correct_answer']
    ordering = ['id']
    list_per_page = 10


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['title']
    filter_horizontal = ['questions']
    ordering = ['id']
    list_per_page = 10


@admin.register(Course)
class TestAdmin(admin.ModelAdmin):
    list_display = ['title']
    filter_horizontal = ['tests']
    ordering = ['id']
    list_per_page = 10