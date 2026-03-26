from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'


from django.urls import path
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import ExampleModel
from .serializers import ExampleModelSerializer

class ExampleModelViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = ExampleModel.objects.all()
        serializer = ExampleModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ExampleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            example = ExampleModel.objects.get(pk=pk)
            serializer = ExampleModelSerializer(example)
            return Response(serializer.data)
        except ExampleModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            example = ExampleModel.objects.get(pk=pk)
            serializer = ExampleModelSerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ExampleModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            example = ExampleModel.objects.get(pk=pk)
            example.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ExampleModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


from django.urls import include

urlpatterns = [
    path('examples/', ExampleModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('examples/<int:pk>/', ExampleModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]


from django.db import models

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


from rest_framework import serializers

class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = '__all__'


# In myproject/settings.py, add 'api' to INSTALLED_APPS
INSTALLED_APPS = [
    ...
    'api',
    ...
]

# In myproject/urls.py, include the api urls
from django.urls import path, include

urlpatterns = [
    ...
    path('api/', include('api.urls')),
    ...
]