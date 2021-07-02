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

    def __str__(self) -> str:
        return str(self.question)


class ResponseModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, null=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()

class ResultModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    total = models.IntegerField()
    authoritarianism = models.PositiveIntegerField()
    exhibitionism = models.PositiveIntegerField()
    superiority = models.PositiveIntegerField()
    claim = models.PositiveIntegerField()
    unscrupulous = models.PositiveIntegerField()
    selfsufficiency = models.PositiveIntegerField()
    vanity = models.IntegerField()
    feature = models.CharField(
        max_length=20, null=True,
        choices=[
            ("authoritarianism","authoritarianism"),
            ("exhibitionism","exhibitionism"),
            ("superiority","superiority"),
            ("claim","claim"),
            ("unscrupulous","unscrupulous"),
            ("selfsufficiency","selfsufficiency"),
            ("vanity","vanity"),
        ]
        )

    def __str__(self) -> str:
        return str(self.username)