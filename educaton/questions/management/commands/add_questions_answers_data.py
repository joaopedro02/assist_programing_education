from django.core.management.base import BaseCommand, CommandError

from questions.models import Question, Answers


class Command(BaseCommand):
    help="add data to app data bank"
    
    def handle(self,*args,**options):
        q=Question(question_text="testando pergunta 1",form=1)
        q.save()
        q.answers_set.create(answers_text="escolha 1",answers_value=1)
        q.answers_set.create(answers_text="escolha 2",answers_value=1)
        
        q=Question(question_text="testando pergunta 2",form = 1 ) 
        q.save()