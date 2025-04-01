from django.urls import path
from .views import vista_cabra
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('galeria/', views.galeria, name='galeria'),
    path('contacto/', views.contacto, name='contacto'),
    path('like/<int:post_id>/', views.dar_like, name='dar_like'),
    path('dislike/<int:post_id>/', views.dar_dislike, name='dar_dislike'),
    path('cabra/', vista_cabra, name='cabra'),

]
