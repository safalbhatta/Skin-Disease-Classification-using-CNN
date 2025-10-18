from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('example/', include('apps.example_app.urls')),  # Include URLs from example_app
]