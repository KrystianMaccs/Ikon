from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),            
    #path("api/v1/users/", include("apps.users.urls")),
    path("api/v1/gallery/", include("apps.gallery.urls")),
]

 