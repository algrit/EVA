from django.contrib import admin

from education.models import Question


# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'question_text', 'correct_answer', 'incorrect_answer1', 'incorrect_answer2',
                    'comment']
    ordering = ['id']