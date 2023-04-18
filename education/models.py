from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=40)
    question_text = models.TextField()
    correct_answer = models.TextField()
    incorrect_answer1 = models.TextField(default='Bad answer 1', blank=True)
    incorrect_answer2 = models.TextField(default='Bad answer 2', blank=True)
    comment = models.TextField(default='Your answer is wrong.', blank=True)

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=40)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=40)
    tests = models.ManyToManyField(Test)

    def __str__(self):
        return self.title
