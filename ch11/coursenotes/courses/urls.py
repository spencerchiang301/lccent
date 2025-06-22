from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('add/', views.course_add, name='course_add'),
]