from django.urls import path

from . import views

urlpatterns = [
    path("index", views.index, name='index'),
    path("about", views.about, name='about'),
    path("hello/<str:name>", views.index, name='hello'),
    path("question/<int:id>", views.question, name='question'),
    path('admin-user', views.admin_user_list, name='adminUserList')
]