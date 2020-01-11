from django.urls import path
from . import views

urlpatterns = [
        path('deshboard/', views.deshboard, name='deshboard'),
]
