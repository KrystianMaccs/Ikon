from django.urls import path

from .views import AlbumsView, AlbumsPhotosView, Photoview


urlpatterns = [
    path('albums/', AlbumsView.as_view(), name='albums'),
    path('albums/<int:pk>/', AlbumsView.as_view(), name='album-detail'),
    path('albums/<int:album_id>/photos/', AlbumsPhotosView.as_view(), name='album-photos'),
    path('albums/<int:album_id>/photos/<int:pk>/', AlbumsPhotosView.as_view(), name='album-photo-detail'),
    path('photos/', PhotoView.as_view(), name='photos')
    path('photos/<int:pk>/', PhotoView.as_view(), name='photo-detail'),
]