from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import QuestionModel
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class QuestionView(LoginRequiredMixin,ListView):
    model = QuestionModel
    template_name = 'questions/list.html'
    context_object_name = "obj"
    login_url = "/#why"

    def get_queryset(self):
        queryset = QuestionModel.objects.all()
        print(queryset[0].id)
        return queryset