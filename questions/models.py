from enum import auto
from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class QuestionModel(models.Model):
    question = models.IntegerField(validators=[
            MaxValueValidator(40),
            MinValueValidator(1)
        ])
    
    answer = models.CharField(max_length=150)
    value = models.IntegerField(choices=[(0,'0'),(1,'1')])

    class Meta():
        pass

class ResponseModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()

class ResultModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    total = models.IntegerField()

