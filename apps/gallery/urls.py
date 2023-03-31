from django.urls import path

from apps.gallery.views import AlbumsView, AlbumsPhotosView

urlpatterns = [
    path('albums/', AlbumsView.as_view(), name='albums'),
    path('albums/<int:album_id>/', AlbumsView.as_view(), name='album-detail'),
    path('albums/<int:album_id>/photos/', AlbumsPhotosView.as_view(), name='album-photos'),
    path('albums/photos/<int:pk>/', AlbumsPhotosView.as_view(), name='album-photo-detail'),
]
