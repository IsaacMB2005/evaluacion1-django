from django.urls import path
from . import views

urlpatterns = [
    path('vista1/', views.vista_uno, name='app1_vista1'),
    path('vista2/', views.vista_dos, name='app1_vista2'),
]

