from django.db import models
from django.utils import timezone


class Poll(models.Model):
    name = models.CharField('название', max_length=55)
    start_date = models.DateTimeField('дата старта', default=timezone.now)
    end_date = models.DateTimeField('дата окончания')
    description = models.TextField('описание')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-start_date',)
        verbose_name_plural = 'опросы'


class Question(models.Model):
    ONE_OPTION = 'one option'
    TEXT_RESPONSE = 'text response'
    MULTILPE_OPTIONS = 'multiple options'

    QUESTION_TYPE_CHOICES = [
        (ONE_OPTION, ONE_OPTION),
        (TEXT_RESPONSE, TEXT_RESPONSE),
        (MULTILPE_OPTIONS, MULTILPE_OPTIONS),
    ]

    text = models.TextField('текст вопроса')
    question_type = models.CharField(
        max_length=25, choices=QUESTION_TYPE_CHOICES,
        default=TEXT_RESPONSE
    )
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE,
        related_name='questions'
    )

    def __str__(self):
        return self.text


class Answer(models.Model):
    answer = models.TextField('ответ')
    user_id = models.IntegerField()
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE,
        related_name='answers'
    )
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE,
        related_name='answers'
    )

    def __str__(self):
        return self.answer

    class Meta:
        ordering = ('question',)
        verbose_name_plural = 'ответы'
        constraints = [
            models.UniqueConstraint(
                fields=['user_id', 'question'],
                name='unique_answer'
            )
        ]
