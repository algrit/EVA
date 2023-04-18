from rest_framework.serializers import ModelSerializer

from education.models import Question


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'question_text']
