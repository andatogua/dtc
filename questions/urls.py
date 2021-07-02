from django.urls import path
from .views import QuestionView,ResultView,ReportView
from questions import views

urlpatterns = [
    path('',QuestionView.as_view(),name="q_list"),
    path('result/', ResultView.as_view(), name='result'),
    path('report/', ReportView.as_view(), name='report')
]