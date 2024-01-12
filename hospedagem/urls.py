from django.urls import path
from .views import Deletar, Criar, Listar, Detalhar, Editar

urlpatterns = [
    path('listar/', Listar.as_view(), name='listar_cliente'),
    path('deletar/<int:pk>/', Deletar.as_view(), name='deletar_cliente'),
    path('editar/<int:pk>/', Editar.as_view(), name='editar_cliente'),
    path('detalhar/', Detalhar.as_view(), name='detalhar_cliente.html'),
    path('criar/', Criar.as_view(), name='criar_cliente'),
]