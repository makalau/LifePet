from django.urls import path
from . import views

urlpatterns = [
    path('', views.consultar, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path("consulta/", views.consultar, name="consultar"),
    path("deletar/<int:id>", views.deletar, name="deletar"),
    path("search/<int:id>", views.search, name="search"),
    path("editar/<int:id>", views.editar, name="editar"),
]
