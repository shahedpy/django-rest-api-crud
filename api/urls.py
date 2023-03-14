from django.urls import path
from .views import TaskList, TaskDetail, ApiOverview
from . import views


urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('', ApiOverview.as_view() ,name = 'api-overview'),
]