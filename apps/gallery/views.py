from rest_framework import generics, permissions

from .models import Albums, Photos
from .serializers import AlbumsSerializer, PhotosSerializer


class AlbumsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AlbumsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.instance.owner != self.request.user:
            raise permissions.PermissionDenied("You are not the owner of this album.")
        serializer.save()


class PhotosListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PhotosSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        album_id = self.kwargs.get('album_id')
        return Photos.objects.filter(album__id=album_id)

    def perform_create(self, serializer):
        album_id = self.kwargs.get('album_id')
        album = Albums.objects.get(id=album_id)
        if album.owner != self.request.user:
            raise permissions.PermissionDenied("You are not the owner of this album.")
        serializer.save(owner=self.request.user, album=album)


class PhotosRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.instance.owner != self.request.user:
            raise permissions.PermissionDenied("You are not the owner of this photo.")
        serializer.save()


