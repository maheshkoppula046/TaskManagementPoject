from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


# router  = DefaultRouter()
# router.register(r'tasks',TaskViews)


urlpatterns = [
    path('tasks/',views.GetCreateTasks,name='GetCreateTasks'),
    path('tasks/<int:pk>/',views.GetUpdateDeleteTask,name='GetUpdateDeleteTask'), 
]