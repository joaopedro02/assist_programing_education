from django.shortcuts import render
from django.http import HttpResponse,  HttpResponseRedirect
from .models import Question,Answers
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db.models import Sum
from autentication.models import perfil

@login_required
def form1(request):
    # estilos de aprendizagem 
        # form = MyForm(request.POST)
        # if form.is_valid():

    answer=Answers.objects.filter(user__username=request.user.get_username())
    questions=Question.objects.exclude(form=2).exclude(answers__id__in=answer)[:5]

    countanswer=answer.filter(question__form=1).count()
    if countanswer >=80 :
        return HttpResponseRedirect(reverse('questions:respondido'))

    print(countanswer)
    print(questions)
    # for q in questions:
    #     print(q.id)
    for q in questions:
        print(q.form)
    porcentagem=(countanswer/80.0)*100.0
    porcentagem_completada="width: " + str(porcentagem)+ "%;"
    print(porcentagem_completada)
    valor_completada=porcentagem
    context = {
        'questions':questions,
        'porcentagem_completada':porcentagem_completada,
        'valor_completada':valor_completada,
    }
    return render(request,'questions/perguntaForm1.html',context)

@login_required
def form2(request):
    # inteligencias multiplas 
    answer=Answers.objects.filter(user__username=request.user.get_username())
    questions=Question.objects.exclude(form=1).exclude(answers__id__in=answer)[:5]
    
    countanswer=answer.filter(question__form=2).count()
    if countanswer>=80:
        return HttpResponseRedirect(reverse('questions:respondido'))

    porcentagem=(countanswer/80.0)*100.0
    porcentagem_completada="width: " + str(porcentagem)+ "%;"
    print(porcentagem_completada)
    valor_completada=porcentagem
    context = {
        'questions':questions,
        'porcentagem_completada':porcentagem_completada,
        'valor_completada':valor_completada,
    }
    return render(request,'questions/perguntaForm2.html',context)

@login_required
def resposta(request):
    formulario=request.POST.get('questionform')
    print("formulario")
    print(formulario)
    print("-")
    answer=Answers.objects.filter(user__username=request.user.get_username())
    countanswer=answer.filter(question__form=int(float(formulario))).count()
    if(countanswer>=80):
        return HttpResponseRedirect(reverse('pagina_do_usuario:pagina_inicial'))

    qid=[]
    resp=[]
    if request.method == "POST":
        qid.append(request.POST.get('questionid1'))
        qid.append(request.POST.get('questionid2'))
        qid.append(request.POST.get('questionid3'))
        qid.append(request.POST.get('questionid4'))
        qid.append(request.POST.get('questionid5'))

        print("id values")
        for i in qid:
            print(i)
        resp.append(request.POST.get('slider1'))
        resp.append(request.POST.get('slider2'))
        resp.append(request.POST.get('slider3'))
        resp.append(request.POST.get('slider4'))
        resp.append(request.POST.get('slider5'))
        print("resp values")
        for r in resp:
            print(r)
        

        for index,i in enumerate(qid):
            answer= Answers.objects.filter(question=int(float(i))).order_by('answers_value')
            answer=answer[int(float(resp[index]))]
            answer.user.add(User.objects.get(username=request.user.get_username()))

        answer=Answers.objects.filter(user__username=request.user.get_username())
        countanswer=answer.filter(question__form=int(float(formulario))).count()
        if(countanswer>=80):# se o usuario tiver respondido todas as questões referentes ao questionario em questao
            if int(float(formulario)) == 1:
                calculo_estilos_de_aprendizagem(request, answer.filter(question__form=int(float(formulario))) )
                pass
            if int(float(formulario)) == 2:
                calculo_inteligencias_multiplas(request, answer.filter(question__form=int(float(formulario))) )
                pass
            return HttpResponseRedirect(reverse('questions:respondido'))
        else:
            if(int(float(formulario))==1):
                return redirect(reverse('questions:form1'))
            else:
                return redirect(reverse('questions:form2'))

    return HttpResponseRedirect(reverse('questions:respondido'))

@login_required
def respondido(request):
    context={
    }
    return render(request,'questions/respondido.html',context)


@login_required
def calculo_inteligencias_multiplas(request,answers):
    a=answers.filter(question__number__gte=1,question__number__lte=10)
    a=a.aggregate(Sum('answers_value'))['answers_value__sum']
    vl=(float(a)/30.0)*100.0

    print(a)

    a=answers.filter(question__number__gte=11,question__number__lte=20)
    a=a.aggregate(Sum('answers_value'))['answers_value__sum']
    lm=(float(a)/30.0)*100.0
    print(a)

    a=answers.filter(question__number__gte=21,question__number__lte=30)
    a=a.aggregate(Sum('answers_value'))['answers_value__sum']
    ve=(float(a)/30.0)*100.0
    print(a)

    a=answers.filter(question__number__gte=31,question__number__lte=40)
    a=a.aggregate(Sum('answers_value'))['answers_value__sum']
    i=(float(a)/30.0)*100.0
    print(a)

    a=answers.filter(question__number__gte=41,question__number__lte=50)
    a=a.aggregate(Sum('answers_value'))['answers_value__sum']
    cc=(float(a)/30.0)*100.0
    print(a)

    a=answers.filter(question__number__gte=51,question__number__lte=60)
    a=a.aggregate(Sum('answers_value'))['answers_value__sum']
    rm=(float(a)/30.0)*100.0
    print(a)

    a=answers.filter(question__number__gte=61,question__number__lte=70)
    a=a.aggregate(Sum('answers_value'))['answers_value__sum']
    intra=(float(a)/30.0)*100.0
    print(a)

    a=answers.filter(question__number__gte=71,question__number__lte=80)
    a=a.aggregate(Sum('answers_value'))['answers_value__sum']  
    n=(float(a)/30.0)*100.0
    print(a)

    request.user.perfil.int_verbal_linguistica=vl
    request.user.perfil.int_musical=rm
    request.user.perfil.int_logico_matematica=lm
    request.user.perfil.int_cinestesico_corporal=cc
    request.user.perfil.int_espacial_visual=ve
    request.user.perfil.int_intrapessoal=intra
    request.user.perfil.int_naturalista=n
    request.user.perfil.int_interpessoal=i
    request.user.perfil.save()

@login_required
def calculo_estilos_de_aprendizagem(request,answers):
    #precisa fazer melhor mas eu estava sem pacienciencia
    #precisa ordena as perguntas na entrada do banco pra gente so ter que fazer querys em intervalos
    # e nao precisar fazer 80 querys
    ativo=[3,5,7,9,13,20,26,27,35,37,41,43,46,48,51,61,67,74,75,77]
    reflexivo=[10,16,18,19,28,31,32,34,36,39,42,44,49,55,58,63,65,69,70,79]
    teorico=[2,4,6,11,15,17,21,23,25,29,33,45,50,54,60,64,66,71,78,80]
    pragmatico=[1,8,12,14,22,24,30,38,40,47,52,53,56,57,59,62,68,72,73,76]
    cont=0.0
    for i in ativo:
        a=answers.get(question__number=i)
        cont=cont+a.answers_value
    at=(cont/60)*100

    cont=0.0
    for i in reflexivo:
        a=answers.get(question__number=i)
        cont=cont + a.answers_value
    re=(cont/60)*100

    cont=0.0
    for i in teorico:
        a=answers.get(question__number=i)
        cont=cont+a.answers_value
    te=(cont/60)*100

    cont=0.0
    for i in pragmatico:
        a=answers.get(question__number=i)
        cont=cont+a.answers_value
    pr=(cont/60)*100

    request.user.perfil.ea_ativo=at
    request.user.perfil.ea_reflexivo=re
    request.user.perfil.ea_pragmatico=pr
    request.user.perfil.ea_teorico=te
    request.user.perfil.save()
    pass