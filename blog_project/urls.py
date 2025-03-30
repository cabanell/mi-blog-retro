from django.contrib import admin
from django.urls import path, include  # ← ESTA LÍNEA ES CLAVE

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

# 🔧 Añade esto aunque DEBUG=False
if settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
