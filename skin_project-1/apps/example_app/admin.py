from django.contrib import admin
from .models import YourModelName  # Replace with your actual model name

@admin.register(YourModelName)  # Replace with your actual model name
class YourModelAdmin(admin.ModelAdmin):  # Replace with your actual model name
    list_display = ('field1', 'field2', 'field3')  # Replace with your actual fields
    search_fields = ('field1', 'field2')  # Replace with your actual fields
    list_filter = ('field1',)  # Replace with your actual fields

# Register your models here
# admin.site.register(YourModelName, YourModelAdmin)  # Uncomment and replace with your actual model name if not using the decorator