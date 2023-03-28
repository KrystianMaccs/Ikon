from django.urls import path
from .views import AlbumsView, PhotosView


urlpatterns = [
    path('albums/', AlbumsView.as_view(), name='albums'),
    path('albums/<uuid:pk>/photos/', PhotosView.as_view(), name='album-photos'),
    path('photos/', PhotosView.as_view(), name='photos'),
    path('photos/<uuid:pk>/', PhotosView.as_view(), name='photo-detail'),
]