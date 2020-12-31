from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import (AnswerViewSet, PollViewSet, QuestionViewSet,
                    UserAnswersViewSet)


v1_router = DefaultRouter()
v1_router.register('polls', PollViewSet, basename='polls')
v1_router.register(
    r'polls/answers/(?P<user_id>\d+)',
    UserAnswersViewSet, basename='user_answers')

question_list = QuestionViewSet.as_view({
    'get': 'list',
    'put': 'partial_update',
    'post': 'create',
    'delete': 'destroy'})

answer_detail = AnswerViewSet.as_view({
    'get': 'retrieve',
    'put': 'partial_update',
    'post': 'create',
    'delete': 'destroy'})

urlpatterns = [
    path('v1/auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/polls/<int:poll_id>/', question_list, name='questions'),
    path(
        'v1/polls/<int:poll_id>/<int:que_id>/', answer_detail, name='answers'),
    path('v1/', include(v1_router.urls)),
]
