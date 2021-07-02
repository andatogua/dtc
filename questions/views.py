from django.http import response
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, DetailView
from .models import QuestionModel, ResponseModel, ResultModel
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import auth
from django.db.models import Count
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist

def getFeature(list):
    feature = ["authoritarianism", "exhibitionism", "superiority", "claim", "unscrupulous", "selfsufficiency", "vanity"]
    major = list[0]
    index = 0
    for i in range(1,len(list)):
        if list[i] > major:
            major = list[i]
            index = i
    return feature[index]


# Create your views here.
class QuestionView(LoginRequiredMixin,ListView):
    model = QuestionModel
    template_name = 'questions/list.html'
    context_object_name = "obj"
    login_url = "/#why"
    queryset = QuestionModel.objects.all()

    def post(self,request,*args,**kwargs):
        total = 0
        authoritarianism = 0
        exhibitionism = 0
        superiority = 0
        claim = 0
        unscrupulous = 0
        selfsufficiency = 0
        vanity = 0
        data = request.POST
        for d in data:
            if d != 'csrfmiddlewaretoken':
                #print('{0}:{1}'.format(d,data[d]))
                id = str(int(d)*2)
                i = int(id)/2
                q = QuestionModel.objects.get(id = id)
                ResponseModel.objects.create(
                    question = q,
                    username = auth.get_user(request),
                    value = data[d]
                )
                total += int(data[d])
                if i < 9 :
                    authoritarianism += int(data[d])
                elif i > 8 and i < 16:
                    exhibitionism += int(data[d])
                elif i > 15 and i < 21:
                    superiority += int(data[d])
                elif i > 20 and i < 29:
                    claim += int(data[d])
                elif i > 28 and i < 34:
                    unscrupulous += int(data[d])
                elif i > 33 and i < 38:
                    selfsufficiency += int(data[d])
                else:
                    vanity += int(data[d])
        ResultModel.objects.create(
            username = auth.get_user(request),
            total = total,
            authoritarianism = authoritarianism,
            exhibitionism = exhibitionism,
            superiority = superiority,
            claim = claim,
            unscrupulous = unscrupulous,
            selfsufficiency = selfsufficiency,
            vanity = vanity,
            feature = getFeature([
                authoritarianism,
                exhibitionism,
                superiority,
                claim,
                unscrupulous,
                selfsufficiency,
                vanity
            ])
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


class ReportView(LoginRequiredMixin,ListView):
    model = ResultModel
    template_name = 'questions/report.html'
    context_object_name = 'obj'
    login_url = "/admin/login/?next=/questions/report/"

    def get(self, request, *args, **kwargs):
        labels = []
        data = []
        total = 0
        try:
            queryset = ResultModel.objects.values('feature').order_by('feature').annotate(count=Count('feature'))
            for q in queryset:
                labels.append(q["feature"])
                data.append(q["count"])
                total += int(q["count"])
            return render(request,self.template_name,{"labels":labels,"data":data,"total":total})
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/')