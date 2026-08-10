from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('dogs.urls', namespace='dogs')),
                path('users/', include('users.urls', namespace='users')),
                path('reviews/', include('reviews.urls', namespace='reviews')),
            ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
