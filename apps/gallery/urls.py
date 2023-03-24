from django.urls import path
from .views import AlbumsListCreateAPIView, AlbumsRetrieveUpdateDestroyAPIView,\
                    PhotosListCreateAPIView, PhotosRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('albums/', AlbumsListCreateAPIView.as_view(), name='album-list'),
    path('albums/<int:pk>/', AlbumsRetrieveUpdateDestroyAPIView.as_view(), name='album-detail'),
    path('albums/<int:album_id>/photos/', PhotosListCreateAPIView.as_view(), name='photo-list'),
    path('photos/<int:pk>/', PhotosRetrieveUpdateDestroyAPIView.as_view(), name='photo-detail'),
]
