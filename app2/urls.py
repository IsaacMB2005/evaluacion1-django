from django.urls import path
from . import views

urlpatterns = [
    path('vista1/', views.vista_uno, name='app2_vista1'),
    path('vista2/', views.vista_dos, name='app2_vista2'),
]