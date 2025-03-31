from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

# Esta parte debe estar al final del archivo:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
