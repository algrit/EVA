from django.contrib import admin

from education.models import Question, Test, Course, CourseSubscription


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
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title']
    filter_horizontal = ['tests']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['id']
    # readonly_fields = ['slug']
    list_per_page = 10


@admin.register(CourseSubscription)
class CourseSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'course', 'sub_time', 'unsub_time', 'active']