from django.urls import path
from .views import AdaptarContenidoView
from .views import AdaptarContenidoView, PublicarContenidoView

urlpatterns = [
    path('adaptar/', AdaptarContenidoView.as_view(), name='adaptar-contenido'),
    path('publicar/', PublicarContenidoView.as_view(), name='publicar-contenido'),
]