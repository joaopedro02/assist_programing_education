from django.contrib import admin

from .models import Question
from .models import Answers

admin.site.register(Question)
admin.site.register(Answers)
# Register your models here.
