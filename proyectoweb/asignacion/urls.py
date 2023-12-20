from django.urls import path
from . import views

urlpatterns = [
    path('Asignacion/', views.procesar_pedido, name='procesar_pedido'),
]
