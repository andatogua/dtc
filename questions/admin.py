from django.contrib import admin
from .models import QuestionModel, ResponseModel

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display=["question","answer","value"]

class ResponseAdmin(admin.ModelAdmin):
    list_display=["question","username","value"]

admin.site.register(QuestionModel,QuestionAdmin)
admin.site.register(ResponseModel,ResponseAdmin)
