from polls.models import Answer, Poll, Question
from rest_framework import serializers


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ('id', 'name', 'start_date', 'end_date', 'description')


class QuestionSerializer(serializers.ModelSerializer):
    poll = serializers.SlugRelatedField(
        slug_field='name', read_only=True
    )

    class Meta:
        model = Question
        fields = ('id', 'poll', 'question_type', 'text',)


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(
        slug_field='text', read_only=True
    )
    poll = serializers.SlugRelatedField(
        slug_field='id', read_only=True
    )

    class Meta:
        model = Answer
        fields = ('poll', 'question', 'user_id', 'answer',)
