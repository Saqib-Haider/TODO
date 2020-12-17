from django.urls import path
from . import views
urlpatterns = [
    path('',views.task_list, name="task_list"),
    path('update_task/<str:pk>/', views.task_update, name="update_task"),
    path('delete_task/<str:pk>/', views.task_delete, name="delete_task"),
]