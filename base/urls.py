from django.urls import path
from . import views


urlpatterns = [
    path('login_page/', views.user_login, name = 'login'),
    path('logout_page/', views.user_logout, name = 'logout'),
    path('register/',views.user_register, name = 'register'),

    path('', views.task_list, name = 'home'),
    path('detail/<int:pk>/', views.task_detail, name = 'detail'),
    path('create-task/', views.create_new_task, name = 'new_task'),
    path('update-task/<int:pk>/', views.update_task, name = 'update_task'),
    path('delete-task/<int:pk>/', views.delete_task, name = 'delete_task'),

]