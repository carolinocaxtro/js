# hospedagem/forms.py

from django import forms
from .models import Cliente, IDCliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'data_entrada', 'data_saida']
        # Poderia adicionar widgets personalizados, labels, help_texts etc., se necessário

class IDClienteForm(forms.ModelForm):
    class Meta:
        model = IDCliente
        fields = ['id_cliente']
        # Adicione outros campos conforme necessário
