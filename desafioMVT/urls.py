from django.urls import path
from desafioMVT import views

urlpatterns = [
   path('familia',views.familia , name='familia'),
]
