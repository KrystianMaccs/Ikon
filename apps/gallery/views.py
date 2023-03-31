from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from .models import Album, Photo
from .serializers import AlbumsSerializer, PhotosSerializer


class AlbumsView(APIView):
    serializer_class = AlbumsSerializer

    def get(self, request):
        albums = Album.objects.all()
        serializer = self.serializer_class(albums, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            album = serializer.save()
            return Response(AlbumsSerializer(album).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        album_id = kwargs.get("pk")
        album = get_object_or_404(Album, pk=kwargs.get("album_id"))
        serializer = self.serializer_class(album, data=request.data)
        if serializer.is_valid():
            album = serializer.save()
            return Response(self.serializer_class(album).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        album_id = kwargs.get("pk")
        album = Album.objects.get(pk=kwargs.get("album_id"))
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbumsPhotosView(APIView):
    serializer_class = PhotosSerializer

    def get(self, request, *args, **kwargs):
        album_id = kwargs.get("album_id")
        photos = Photo.objects.filter(album__id=album_id)
        serializer = self.serializer_class(photos, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        album_id = kwargs.get("album_id")
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            album = get_object_or_404(Album, pk=kwargs.get("album_id"))
            serializer.save(album=album)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        photo_id = kwargs.get("pk")
        photo = Photo.objects.get(pk=photo_id)
        serializer = self.serializer_class(photo, data=request.data)
        if serializer.is_valid():
            photo = serializer.save()
            return Response(serializer_class(photo).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        photo_id = kwargs.get("pk")
        photo = Photo.objects.get(pk=photo_id)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
Instead of explicitly passing in pk and album_id directly to the functions, 
all you need are args and kwargs. You can get the value of pk or album_id 
by doing:

pk = kwargs.get("pk")
album_id = kwargs.get("album_id")
"""