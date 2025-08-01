from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Your app's URLs
    path('', include('django.contrib.auth.urls')),  # 🔥 This is what adds 'logout', 'login', etc.
]
