from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('lb/', include('lb.urls')),
    path('admin/', admin.site.urls),
]
