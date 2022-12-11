from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from portafolio.forms import RegistroUserForm
from portafolio.models import Perfil, Project
from django.urls import reverse 
from django.views import View
from portafolio.forms import PortafolioForm
# Create your views here.

class PortafolioP(ListView):
    model = Perfil
    template_name = 'index.html'
    def get(self, request):
      portafolios = Project.objects.all()
      data = {
          'portafolios': portafolios
      }
      return render(request, 'index.html', data)

class registro_userView(CreateView):
    model = User
    template_name = 'registration/registro_user.html'
    form_class = RegistroUserForm
    def get_success_url(self):
        return reverse('login')


class portafolioView(View):
    model = Project
    template_name = 'portafolioNew.html'
    context ={}
    context['form'] = PortafolioForm()
    
    def get(self, request):
        return render(request, self.template_name, self.context)
    def post (self, request): 
        form =PortafolioForm(request.POST)
        user=request.user
        print('--------5--------')
        if form.is_valid():
            print('-----------------')
            proyecto = Project.objects.create(titulo =form.cleaned_data['titulo'],descripcion=form.cleaned_data['descripcion'], foto=form.cleaned_data['foto'],  url=form.cleaned_data['url'], tags=form.cleaned_data['tags'], user_id = user.id)
            return redirect('index')
        else:
            return render(request, self.template_name, {'form':form})

