from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apptelas.urls')),
    # path('users/', include('appuser.urls')),
    # path('api/', include('api.urls')),
]
