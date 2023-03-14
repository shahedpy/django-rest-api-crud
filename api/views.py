from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import TaskSerializer
from .models import Task


class ApiOverview(generics.GenericAPIView):
    """
    API Overview
    ------------
    This API allows you to create, read, update, and delete tasks.

    Endpoints
    ---------
    - List all tasks: {base_url}/tasks/ (GET)
    - Create a new task: {base_url}/tasks/ (POST)
    - Retrieve a task by ID: {base_url}/tasks/<int:pk>/ (GET)
    - Update a task by ID: {base_url}/tasks/<int:pk>/ (PUT/PATCH)
    - Delete a task by ID: {base_url}/tasks/<int:pk>/ (DELETE)

    """
    def get(self, request, *args, **kwargs):
        # Use Django REST Framework's `reverse` function to generate URLs for the endpoints
        api_urls = {
            'List': reverse('task-list', request=request),
            'Create': reverse('task-list', request=request),
            'Retrieve': reverse('task-detail', args=[1], request=request),
            'Update': reverse('task-detail', args=[1], request=request),
            'Delete': reverse('task-detail', args=[1], request=request),
        }

        # Return the API URLs as a JSON response
        return Response(api_urls)

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer