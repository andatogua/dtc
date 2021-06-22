from django.contrib import admin
from .models import QuestionModel, ResponseModel, ResultModel

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display=["question","answer","value"]

class ResponseAdmin(admin.ModelAdmin):
    list_display=["question","username","value"]

class ResultAdmin(admin.ModelAdmin):
    list_display=["username","date","total"]

admin.site.register(QuestionModel,QuestionAdmin)
admin.site.register(ResponseModel,ResponseAdmin)
admin.site.register(ResultModel,ResultAdmin)
