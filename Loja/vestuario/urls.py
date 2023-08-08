from django.urls import path

from . import views 

urlpatterns = [
    path("", views.index, name='index'),
    path("pagina/", views.pagina, name="pagina"),
    path("catalogo/", views.catalogo, name="catalogo")
]