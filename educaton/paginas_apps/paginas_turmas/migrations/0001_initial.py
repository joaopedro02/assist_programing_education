# Generated by Django 2.2 on 2019-07-03 18:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Turmas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cor', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=1000)),
                ('alunos', models.ManyToManyField(related_name='turmas_onde_sou_aluno', to=settings.AUTH_USER_MODEL)),
                ('mestres', models.ManyToManyField(related_name='turmas_onde_sou_mestre', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
