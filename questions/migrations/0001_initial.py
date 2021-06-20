# Generated by Django 2.2 on 2021-06-19 21:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_question', models.IntegerField(validators=[django.core.validators.MaxValueValidator(40), django.core.validators.MinValueValidator(1)])),
                ('_answer', models.CharField(max_length=150)),
                ('_value', models.IntegerField(choices=[(0, '0'), (1, '1')])),
            ],
        ),
        migrations.CreateModel(
            name='ResultModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_date', models.DateTimeField(auto_now=True)),
                ('_total', models.IntegerField()),
                ('_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResponseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_value', models.IntegerField()),
                ('_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
