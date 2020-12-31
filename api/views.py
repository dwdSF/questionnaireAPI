from django.shortcuts import get_object_or_404
from django.utils import timezone
from polls.models import Answer, Poll, Question
from rest_framework import filters, serializers, viewsets

from .permissions import AdminOrReadOnly, AdminOrReadOnlyOrAnswer, ReadOnly
from .serializers import AnswerSerializer, PollSerializer, QuestionSerializer
from .viewsets import CreateListViewSet, ListViewSet


class PollViewSet(CreateListViewSet):

    serializer_class = PollSerializer
    permission_classes = (AdminOrReadOnly,)

    def get_queryset(self):
        queryset = Poll.objects.filter(end_date__gt=timezone.now())
        return queryset


class QuestionViewSet(viewsets.ModelViewSet):

    permission_classes = (AdminOrReadOnly,)
    lookup_url_kwarg = 'poll_id'

    def get_queryset(self):
        if self.request.method in ('DELETE', 'PUT'):
            queryset = Poll.objects.all()
            return queryset
        poll = get_object_or_404(Poll, pk=self.kwargs['poll_id'])
        queryset = poll.questions.all()
        return queryset

    def get_serializer_class(self):
        if self.request.method in ('DELETE', 'PUT'):
            return PollSerializer
        return QuestionSerializer

    def perform_update(self, serializer):
        if 'start_date' in self.request.data:
            raise serializers.ValidationError('Вы не можете изменять дату начала опроса.') # noqa
        serializer.save()

    def perform_create(self, serializer):
        poll = get_object_or_404(Poll, pk=self.kwargs['poll_id'])
        serializer.save(poll=poll)


class AnswerViewSet(viewsets.ModelViewSet):

    permission_classes = (AdminOrReadOnlyOrAnswer,)
    lookup_url_kwarg = 'que_id'

    def get_queryset(self):
        poll = get_object_or_404(Poll, pk=self.kwargs['poll_id'])
        queryset = poll.questions.all()
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AnswerSerializer
        return QuestionSerializer

    def perform_create(self, serializer):
        user_id = self.request.data.get('user_id')
        question = get_object_or_404(Question, pk=self.kwargs['que_id'])
        if Answer.objects.filter(user_id=user_id, question=question).exists():
            raise serializers.ValidationError('Пользователь с таким id уже давал ответ на этот вопрос!') # noqa

        serializer.save(question=question, poll=question.poll)


class UserAnswersViewSet(ListViewSet):

    serializer_class = AnswerSerializer
    permission_classes = (ReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=poll__id',)

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Answer.objects.filter(user_id=user_id)
        return queryset
