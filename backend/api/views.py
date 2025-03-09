from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializers

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# class TaskViews(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers
@api_view(['GET','POST'])
def GetCreateTasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializers(tasks, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def GetUpdateDeleteTask(request,pk):
    if request.method == 'GET':
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializers(task)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializers(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages,status=status.HTTP_204_NO_CONTENT)

    if request.method == 'DELETE':
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    