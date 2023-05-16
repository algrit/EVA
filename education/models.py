from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Question(models.Model):
    title = models.CharField(max_length=40)
    question_text = models.TextField()
    correct_answer = models.TextField()
    incorrect_answer1 = models.TextField(default='Bad answer 1', blank=True)
    incorrect_answer2 = models.TextField(default='Bad answer 2', blank=True)
    comment = models.TextField(default='Your answer is wrong.', blank=True)

    def __str__(self):
        return f'{self.title} ({self.id})'


class Test(models.Model):
    title = models.CharField(max_length=40)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f'{self.title} ({self.id})'

    def get_url(self):
        return reverse('test_details', args=(self.id, ))


class Course(models.Model):
    title = models.CharField(max_length=40)
    tests = models.ManyToManyField(Test, verbose_name='tests in course', related_name='courses')
    slug = models.SlugField(default='')

    def __str__(self):
        return f'{self.title} ({self.id})'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('course_details', args=(self.slug, ))




class CourseSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    sub_time = models.DateTimeField(auto_now_add=True)
    unsub_time = models.DateTimeField(null=True, default=None, editable=False)
    active = models.BooleanField(default=True, editable=False)

    def __str__(self):
        return f'{self.user}({self.user.id}) - {self.course}({self.course.id})'

