from django.http import response
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import QuestionModel, ResponseModel
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import auth

# Create your views here.
class QuestionView(LoginRequiredMixin,ListView):
    model = QuestionModel
    template_name = 'questions/list.html'
    context_object_name = "obj"
    login_url = "/#why"
    queryset = QuestionModel.objects.all()

    def post(self,request,*args,**kwargs):
        data = request.POST
        for d in data:
            if d != 'csrfmiddlewaretoken':
                #print('{0}:{1}'.format(d,data[d]))
                id = str(int(d)*2)
                q = QuestionModel.objects.get(id = id)
                ResponseModel.objects.create(
                    question = q,
                    username = auth.get_user(request),
                    value = data[d]
                )
        return HttpResponseRedirect('/')
        
