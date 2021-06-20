from django.contrib import admin
from .models import QuestionModel

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display=["question","answer","value"]

admin.site.register(QuestionModel,QuestionAdmin)
