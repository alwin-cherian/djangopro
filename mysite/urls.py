from django.contrib import admin
from django.urls import path,include
from film import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home),
    # path('home/', include('film.url')),
    path('', include('film.url'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

