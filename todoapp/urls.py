from django.urls import path
from . import views
from .views import TaskUpdateView, TaskDeleteView, TaskListApi, TaskDetailApi, TaskListView
urlpatterns = [
    path('',TaskListView.as_view(), name="task_list"),
    #path('',views.task_list, name="task_list"),
    #path('update_task/<str:pk>/', views.task_update, name="update_task"),
    path('update_task/<int:id>/', TaskUpdateView.as_view(), name='update_task'),
    #path('delete_task/<str:pk>/', views.task_delete, name="delete_task"),
    path('delete_task/<int:id>/', TaskDeleteView.as_view(), name="delete_task"),
    path('api/',TaskListApi.as_view(), name='list&create'),
    path('api/<int:id>/',TaskDetailApi.as_view(), name='deelete%update'),
]