from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, ListView, DeleteView, CreateView
from hospedagem.models import Cliente
from .forms import ClienteForm, IDClienteForm


class Detalhar(DetailView):
    model = Cliente
    template_name = 'detalhar_template'

class Listar(ListView):
    model = Cliente
    template_name = 'listar_template'
    form_class = ClienteForm


class Editar(UpdateView):
    model = Cliente
    template_name = 'editar_template'


class Deletar(DeleteView):
    model = Cliente
    template_name = 'deletar_template'


class Criar(CreateView):
    model = Cliente
    template_name = 'criar_cliente'
    form_class = ClienteForm







# Create your views here.
