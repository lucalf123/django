from django.urls import path
from .views import index, produtos, clientes, exemplo

urlpatterns = [
    path('', index, name='index'),
    path('clientes', clientes, name='clientes'),
    path('produtos/<int:pk>', produtos, name='produtos'),
    path('exemplo', exemplo, name='exemplo'),
]