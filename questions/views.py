from django.http import response
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, DetailView
from .models import QuestionModel, ResponseModel, ResultModel
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import auth
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class QuestionView(LoginRequiredMixin,ListView):
    model = QuestionModel
    template_name = 'questions/list.html'
    context_object_name = "obj"
    login_url = "/#why"
    queryset = QuestionModel.objects.all()

    def post(self,request,*args,**kwargs):
        total = 0
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
                total += int(data[d])
        ResultModel.objects.create(
            username = auth.get_user(request),
            total = total
        )
        return HttpResponseRedirect('/questions/result/')

    def get(self,request,*args,**kwargs):
        username = auth.get_user(request)
        try:
            obj = ResultModel.objects.get(username=username)
            return HttpResponseRedirect('/questions/result/')

        except ObjectDoesNotExist:
            return render(request,self.template_name,{"obj":self.queryset})

        
#def ResultView(request):
#    return render(request,'questions/result.html')

class ResultView(LoginRequiredMixin,ListView):
    model = ResultModel
    template_name = 'questions/result.html'
    context_object_name = 'obj'
    login_url = "/#why"

    def get(self,request,*args,**kwargs):
        username = auth.get_user(request)
    
        try:
            queryset = ResultModel.objects.get(username=username)
            deg = queryset.total - 20
            return render(request,self.template_name,{"obj":queryset,"deg":deg})

        except ObjectDoesNotExist:
            
            return HttpResponseRedirect('/questions/')
