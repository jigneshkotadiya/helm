from django.urls import path
from . import views

app_name = 'engineering'
urlpatterns = [
        path('deshboard/', views.deshboard, name='deshboard'),
        path('deshboard/<int:exam_id>/', views.detail, name='detail'),

]
