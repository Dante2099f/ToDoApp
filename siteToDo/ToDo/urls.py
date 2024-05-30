from django.urls import path
from . import views
from .views import CustomLoginview, TaskList,TaskDelete, TaskDetail,RegisterPage, TaskCreate, TaskUpdate
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginview.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),

]