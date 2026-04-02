from rest_framework import permissions
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from django.urls import path

schema_view = get_schema_view(title='My API', permission_classes=(permissions.AllowAny,))
swagger_view = get_swagger_view(title='My API Documentation', url='/api/docs/')

urlpatterns = [
    path('docs/', swagger_view, name='swagger-docs'),
    path('schema/', schema_view, name='api-schema'),
]