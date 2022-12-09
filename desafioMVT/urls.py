from django.urls import path
from desafioMVT import views

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('familia',views.familia , name='familia'),
]
