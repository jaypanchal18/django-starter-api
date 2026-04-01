from django.contrib import admin
from .models import YourModel1, YourModel2  # Replace with your actual model names

class YourModel1Admin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')  # Replace with your actual fields
    search_fields = ('field1', 'field2')  # Replace with your actual fields
    list_filter = ('field3',)  # Replace with your actual fields

class YourModel2Admin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Replace with your actual fields
    search_fields = ('field1',)  # Replace with your actual fields
    list_filter = ('field2',)  # Replace with your actual fields

admin.site.register(YourModel1, YourModel1Admin)
admin.site.register(YourModel2, YourModel2Admin)