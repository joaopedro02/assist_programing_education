# Generated by Django 2.2 on 2019-05-04 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='answers_text',
        ),
        migrations.AddField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
