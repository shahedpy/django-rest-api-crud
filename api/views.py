from rest_framework import generics, authentication, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import StudentSerializer
from .models import Students


class ApiOverview(generics.GenericAPIView):
    """
    API Overview
    ------------
    This API allows you to create, read, update, and delete tasks.

    Endpoints
    ---------
    - List all students: {base_url}/students/ (GET)
    - Create a new student: {base_url}/students/ (POST)
    - Retrieve a students by ID: {base_url}/students/<int:pk>/ (GET)
    - Update a student by ID: {base_url}/students/<int:pk>/ (PUT/PATCH)
    - Delete a student by ID: {base_url}/students/<int:pk>/ (DELETE)

    """

    def get(self, request):
        api_urls = {
            'List': reverse('students-list', request=request),
            'Create': reverse('students-list', request=request),
            'Retrieve': reverse('student-detail', args=[1], request=request),
            'Update': reverse('student-detail', args=[1], request=request),
            'Delete': reverse('student-detail', args=[1], request=request),
        }

        return Response(api_urls)


class StudentList(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
