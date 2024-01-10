from django.urls import path
from .views import Deletar, Criar, Listar, Detalhar, Editar

urlpatterns = [
    path('', Listar.as_view(), name='listar_cliente.html'),
    path('deletar/', Deletar.as_view(), name='deletar_cliente.html'),
    path('editar/', Editar.as_view(), name='editar_cliente.html'),
    path('detalhar/', Detalhar.as_view(), name='detalhar_cliente.html'),
    path('criar/', Criar.as_view(), name='criar_cliente.html'),
]