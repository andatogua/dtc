from django.urls import path
from .views import QuestionView,ResultView
from questions import views

urlpatterns = [
    path('',QuestionView.as_view(),name="q_list"),
    path('result/', ResultView.as_view(), name='result')
]