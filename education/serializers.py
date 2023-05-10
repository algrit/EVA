# from rest_framework.serializers import ModelSerializer
#
# from education.models import Question, Course, Test
#
#
# class QuestionSerializer(ModelSerializer):
#     class Meta:
#         model = Question
#         fields = ['title', 'question_text']
#
#
# class TestSerializer(ModelSerializer):
#     class Meta:
#         model = Test
#         fields = ['title']
#
#
# class CourseSerializer(ModelSerializer):
#     class Meta:
#         model = Course
#         # fields = ['title']
#         fields = '__all__'
