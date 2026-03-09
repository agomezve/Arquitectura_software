
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('app_gestion_taller.urls')),
]