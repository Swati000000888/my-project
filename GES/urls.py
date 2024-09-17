from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ges/admin/', admin.site.urls),
    path('ges/', include('power.urls')),
]

