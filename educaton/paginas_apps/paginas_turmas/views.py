from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from questions.models import Answers
from .models import Turmas
from django.views.generic.edit import FormView
from .forms import Add_turma
from .forms import Cria_turma
from django.contrib.auth.models import User
from .BarChart_intMultiplass import BarChart
from pygal.style import BlueStyle
from .BarChart_estAprendii import BarChart_estAprendizagem
from django.shortcuts import redirect


class pagina_inicial(LoginRequiredMixin,TemplateView):# pagina que mostra todas as turmas de um usuario
    template_name="paginas_turmas/pagina_das_turmas.html"

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context["form"].is_valid():
            print ("yes done!!")
            codigo_da_turma=context["form"].cleaned_data['cod_turma']
            T=Turmas.objects.filter(id=codigo_da_turma)
            T[0].alunos.add(self.request.user)
            return redirect("/turmas/")
        else:
            context["form_error"] = True
        return super(TemplateView, self).render_to_response(context)
   
    
    def get_context_data(self, *args ,**kwargs):

        # answer=Answers.objects.filter(user__username=self.request.user.get_username())
        context = super(pagina_inicial, self).get_context_data(*args,**kwargs)
        form = Add_turma(self.request.POST or None)  # instance= None
        turmas=Turmas.objects.filter(alunos=self.request.user.id)
        turmasm=Turmas.objects.filter(mestres=self.request.user.id)
        
        context["form"] = form
        context["form_error"]= False
        context["turmas"]=turmas
        context["turmasm"]=turmasm
        return context
        
class turma(LoginRequiredMixin,TemplateView):# mostra informações de uma turma em especifico
    template_name="paginas_turmas/pagina_de_uma_turma.html"

    
    def get_context_data(self, *args ,**kwargs):
        print("cheguei aqui")
        turma_id=kwargs['turma_id']
        print(turma_id)

        t=Turmas.objects.filter(pk=turma_id)
        alun=t[0].alunos.all()
        
        c=t[0].mestres.filter(pk=self.request.user.id)
        mestre=False
        if c:
            mestre=True
        #media das inteligencias e estilos de aprendizagem da turma
        int_verbal=0
        int_musical=0
        int_logic=0
        int_cinestesico=0
        int_espacial=0
        int_intrapessoal=0
        int_naturalista=0
        int_interpessoal=0
        e_ativo=0
        e_reflexivo=0
        e_pragmatico=0
        e_teorico=0
        cont_int=0
        cont_est=0
        for a in alun:
            if a.perfil.f_int:
                cont_int+=1
                int_verbal+=a.perfil.int_verbal_linguistica
                int_musical+=a.perfil.int_musical
                int_logic+=a.perfil.int_logico_matematica
                int_cinestesico+=a.perfil.int_cinestesico_corporal
                int_espacial+=a.perfil.int_espacial_visual
                int_intrapessoal+=a.perfil.int_intrapessoal
                int_naturalista+=a.perfil.int_naturalista
                int_interpessoal+=a.perfil.int_interpessoal
            if a.perfil.f_est:
                cont_est+=1
                e_ativo+=a.perfil.ea_ativo
                e_reflexivo+=a.perfil.ea_reflexivo
                e_pragmatico+=a.perfil.ea_pragmatico
                e_teorico+=a.perfil.ea_teorico
        if cont_int>0:
            int_verbal=int_verbal/cont_int
            int_musical=int_musical/cont_int
            int_logic=int_logic/cont_int
            int_cinestesico=int_cinestesico/cont_int
            int_espacial=int_espacial/cont_int
            int_intrapessoal=int_intrapessoal/cont_int
            int_naturalista=int_naturalista/cont_int
            int_interpessoal=int_interpessoal/cont_int
        if cont_est>0:
            e_ativo=e_ativo/cont_est
            e_reflexivo=e_reflexivo/cont_est
            e_pragmatico=e_pragmatico/cont_est
            e_teorico=e_teorico/cont_est
        # contagem dos alunos por inteligencia, levando-se em consideração a maior inteligência
        cont_int=0
        cont_est=0
        inteligencia=[]
        inteligenciaT=[0]*8
        estilos=[]
        estilosT=[0]*5
        for a in alun:
            inteligencia.clear()
            estilos.clear()
            if a.perfil.f_int:
                cont_int+=1
                inteligencia.append(a.perfil.int_verbal_linguistica)
                inteligencia.append(a.perfil.int_musical)
                inteligencia.append(a.perfil.int_logico_matematica)
                inteligencia.append(a.perfil.int_cinestesico_corporal)
                inteligencia.append(a.perfil.int_espacial_visual)
                inteligencia.append(a.perfil.int_intrapessoal)
                inteligencia.append(a.perfil.int_naturalista)
                inteligencia.append(a.perfil.int_interpessoal)
                aux=inteligencia[0]
                aux2=0
                for i,n in enumerate(inteligencia) :
                    if aux>n:
                        aux=n
                        aux2=i
                inteligenciaT[aux2]+=1
            if a.perfil.f_est:
                cont_est+=1
                estilos.append(a.perfil.ea_ativo)
                estilos.append(a.perfil.ea_reflexivo)
                estilos.append(a.perfil.ea_pragmatico)
                estilos.append(a.perfil.ea_teorico)
                aux=estilos[0]
                aux2=0
                for i,n in enumerate(estilos) :
                    if aux>n:
                        aux=n
                        aux2=i
                estilosT[aux2]+=1
        if cont_int>0:
            for i,n in enumerate(inteligenciaT):
                inteligenciaT[i]=(n/cont_int)*100.0
        if cont_est>0:
            for i,n in enumerate(estilosT):
                estilosT[i]=(n/cont_est)*100.0

        context = super(turma, self).get_context_data(*args,**kwargs)
        
        grafico_int = BarChart(
            print_zeroes=False,
            height=400,
            width=590,
            explicit_size=True,
            style=BlueStyle(
                  font_family='googlefont:Roboto',
                  value_colors=('black',)),
            show_y_guides=False,
            include_x_axis=False,
            print_values=True,
            print_values_position='top'
            
        )
        grafico_int.set_title('Número de alunos de acordo com o tipo de inteligência predominante em porcentagem.')

        grafico_estilos=BarChart_estAprendizagem(
            print_zeroes=False,
            height=400,
            width=590,
            explicit_size=True,
            style=BlueStyle(
                  font_family='googlefont:Roboto',
                  value_colors=('black',)),
            show_y_guides=False,
            include_x_axis=False,
            print_values=True,
            print_values_position='top'
            
        )

        grafico_estilos.set_title('Número de alunos de acordo com o estilo de aprendizagem predominante em porcentagem.')
        # Call the `.generate()` method on our chart object
        # and pass it to template context.
        context['turma']=t[0]
        context['mestre']=mestre
        context['alunos']=alun
        #context['grafico_int'] = grafico_int.generate(int_verbal, int_musical, int_logic, int_cinestesico, int_espacial, int_intrapessoal, int_naturalista, int_interpessoal)
        context['grafico_int'] = grafico_int.generate(inteligenciaT[0],inteligenciaT[1],inteligenciaT[2],inteligenciaT[3],inteligenciaT[4],inteligenciaT[5],inteligenciaT[6],inteligenciaT[7])
        #context['grafico_estilos'] = grafico_estilos.generate(e_ativo, e_reflexivo, e_pragmatico, e_teorico)
        context['grafico_estilos'] = grafico_estilos.generate(estilosT[0],estilosT[1],estilosT[2],estilosT[3])
        
        return context

class cria_turma(LoginRequiredMixin, FormView):# pagina para criar uma nova turma
    template_name = 'paginas_turmas/cria_turma.html'
    form_class = Cria_turma
    success_url = '/turmas/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        nome=form.cleaned_data['nome']
        descricao=form.cleaned_data['descricao']
        # cor=form.cleaned_data['star_color']
        T=Turmas(nome=nome,descricao=descricao)
        T.save()
        T.mestres.add(self.request.user)
        return super().form_valid(form)
    pass


class addturma():
    pass