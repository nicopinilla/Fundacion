from django.urls import path
from .views import home, registro, iniciar_sesion, aportador
 
urlpatterns = [
    path('', home, name="home"),
    path('registro/<action>/<id>', registro, name="registro"),
    path('iniciar_sesion/<action>/<id>',iniciar_sesion, name="iniciar_sesion"),
    path('aportador>',aportador, name="aportador")
]
