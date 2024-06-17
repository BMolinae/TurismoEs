from django.urls import path
from . import views

urlpatterns = [
    path('servicios/', views.listar_servicios, name='listar_servicios'),
    path('', views.listar_servicios, name='listar_servicios'),
    path('agregar-servicio/', views.agregar_servicio, name='agregar_servicio'),
    
]