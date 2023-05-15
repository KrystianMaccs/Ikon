"""from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from .models import Album, Photo
from .serializers import AlbumsSerializer, PhotosSerializer

from apps.common.permissions import IsPhotographer



class AlbumsView(APIView):
    """
    API endpoint that allows albums to be viewed or edited.
    """
    serializer_class = AlbumsSerializer

    def get(self, request):
        albums = Album.objects.all()
        serializer = self.serializer_class(albums, many=True)
        return Response(serializer.data)

    def post(self, request):
        permission_classes = [IsAuthenticated, IsPhotographer]
        if not request.user.profile.is_photgrapher:
            return Response({"message": "Only Photographers can create albums"}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            album = serializer.save()
            return Response(AlbumsSerializer(album).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated, IsPhotographer]
        if not request.user.profile.is_photographer:
            return Response({"message": "Only Photographers can update photos"}, status=status.HTTP_403_FORBIDDEN)
        album_id = kwargs.get("pk")
        album = get_object_or_404(Album, pk=kwargs.get("album_id"))
        serializer = self.serializer_class(album, data=request.data)
        if serializer.is_valid():
            album = serializer.save()
            return Response(self.serializer_class(album).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated, IsPhotographer]
        if not request.user.profile.is_photographer:
            return Response({"message": "Only Photographers can update photos"}, status=status.HTTP_403_FORBIDDEN)
        album_id = kwargs.get("pk")
        album = Album.objects.get(pk=kwargs.get("album_id"))
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbumsPhotosView(APIView):
    """
    API endpoint that allows photos to be viewed or edited.
    """
    serializer_class = PhotosSerializer

    def get(self, request, *args, **kwargs):
        album_id = kwargs.get("album_id")
        photos = Photo.objects.filter(album__id=album_id)
        serializer = self.serializer_class(photos, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated, IsPhotographer]
        album_id = kwargs.get("album_id")
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            album = get_object_or_404(Album, pk=kwargs.get("album_id"))
            serializer.save(album=album)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated, IsPhotographer]
        photo_id = kwargs.get("pk")
        photo = Photo.objects.get(pk=photo_id)
        serializer = self.serializer_class(photo, data=request.data)
        if serializer.is_valid():
            photo = serializer.save()
            return Response(serializer_class(photo).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated, IsPhotographer]
        photo_id = kwargs.get("pk")
        photo = Photo.objects.get(pk=photo_id)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhotoView(APIView):
    serializer_class = PhotosSerializer
    
    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            return Response({"message": "Photo does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        def get(self, request, pk):
            photo = self.get_object(pk)
            serializer = serializer_class(photo)
            return Response(serializer.data)
        
        def put(self, request, pk):
            if not request.user.profile.is_photographer:
                return Response({"message": "Only Photographers can update photos"}, status=status.HTTP_404_NOT_FOUND)
            photo = self.get_object(pk)
            serializer = serializer_class(photo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self, request, pk):
            if not request.profile.is_photographer:
                return Response({"message": "Only Photographers can delete photos"}, status=status.HTTP_400_FORBIDDEN)
            photo = self.get_object(pk)
            photo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
"""



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from .models import Album, Photo
from .serializers import AlbumsSerializer, PhotosSerializer

from apps.common.permissions import IsPhotographer


class AlbumsView(APIView):
    """
    API endpoint that allows albums to be viewed or edited.
    """
    serializer_class = AlbumsSerializer
    permission_classes = [IsAuthenticated, IsPhotographer]

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

    def put(self, request, album_id):
        album = get_object_or_404(Album, pk=album_id)
        serializer = self.serializer_class(album, data=request.data)
        if serializer.is_valid():
            album = serializer.save()
            return Response(self.serializer_class(album).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, album_id):
        album = get_object_or_404(Album, pk=album_id)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbumsPhotosView(APIView):
    """
    API endpoint that allows photos in an album to be viewed or edited.
    """
    serializer_class = PhotosSerializer
    permission_classes = [IsAuthenticated, IsPhotographer]

    def get(self, request, album_id):
        photos = Photo.objects.filter(album__id=album_id)
        serializer = self.serializer_class(photos, many=True)
        return Response(serializer.data)

    def post(self, request, album_id):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            album = get_object_or_404(Album, pk=album_id)
            serializer.save(album=album)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, photo_id):
        photo = get_object_or_404(Photo, pk=photo_id)
        serializer = self.serializer_class(photo, data=request.data)
        if serializer.is_valid():
            photo = serializer.save()
            return Response(self.serializer_class(photo).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, photo_id):
        photo = get_object_or_404(Photo, pk=photo_id)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhotoView(APIView):
    """
    API endpoint that allows photos to be viewed or edited.
    """
    serializer_class = PhotosSerializer
    permission_classes = [IsAuthenticated, IsPhotographer]

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            return Response({"message": "Photo does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        photo = self.get_object(pk)
        serializer = self.serializer_class(photo)
        return Response(serializer.data)

    def list(self, request):
        photos = Photo.objects.all()
        serializer = self.serializer_class(photos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            photo = serializer.save()
            return Response(PhotoSerializer(photo).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        photo = self.get_object(pk)
        serializer = self.serializer_class(photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        photo = self.get_object(pk)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

