from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, ListView, DeleteView, CreateView
from hospedagem.models import Cliente
from .forms import ClienteForm, IDClienteForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

class Detalhar(DetailView):
    model = Cliente
    template_name = 'listar_cliente.html'


class Listar(ListView):
    model = Cliente
    template_name = 'listar_clientes.html'
    context_object_name = 'clientes'

    
    

    
class Editar(UserPassesTestMixin,UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'editar_cliente.html'
    
    def test_func(self):
        return self.request.user.is_superuser
    


class Deletar(DeleteView):
    model = Cliente
    template_name = 'deletar_template.html'
    success_url = reverse_lazy('listar_cliente') 


class Criar(CreateView):
    model = Cliente
    template_name = 'criar_cliente.html'
    form_class = ClienteForm

def test_func(self):
        return self.request.user.is_superuser






# Create your views here.
