from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('add/', views.course_add, name='course_add'),
    path('<int:pk>/edit/', views.course_edit, name='course_edit'),
    path('<int:pk>/delete/', views.course_delete, name='course_delete'),

    # ⬇️ 新增 Note 功能
    path('<int:course_id>/notes/', views.note_list, name='note_list'),
    path('<int:course_id>/notes/add/', views.note_add, name='note_add'),
    path('<int:course_id>/notes/<int:note_id>/edit/', views.note_edit, name='note_edit'),
    path('<int:course_id>/notes/<int:note_id>/delete/', views.note_delete, name='note_delete'),
]