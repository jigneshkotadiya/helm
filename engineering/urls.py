from django.urls import path
from . import views

app_name = 'engineering'
urlpatterns = [
        path('deshboard/', views.deshboard, name='deshboard'),
        path('deshboard/<int:exam_id>/', views.detail, name='detail'),
        path('deshboard/fom/', views.post_new, name='fom'),
        path('ajax/load-semester/', views.load_semester, name='ajax_load_semester'),
        path('ajax/load-subject/', views.load_subject, name='ajax_load_subject'),

]
