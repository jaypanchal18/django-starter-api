from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = MyModel.objects.all()
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            instance = MyModel.objects.get(pk=pk)
            serializer = MyModelSerializer(instance)
            return Response(serializer.data)
        except MyModel.DoesNotExist:
            raise NotFound(detail="Object not found", code=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            instance = MyModel.objects.get(pk=pk)
            serializer = MyModelSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MyModel.DoesNotExist:
            raise NotFound(detail="Object not found", code=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            instance = MyModel.objects.get(pk=pk)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MyModel.DoesNotExist:
            raise NotFound(detail="Object not found", code=status.HTTP_404_NOT_FOUND)