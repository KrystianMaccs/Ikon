from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Albums, Photos
from .serializers import AlbumsSerializer, PhotosSerializer


class AlbumsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        albums = Albums.objects.filter(owner=request.user)
        serializer = AlbumsSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlbumsSerializer(data=request.data)
        if serializer.is_valid():
            album = serializer.save(owner=request.user)
            return Response(AlbumsSerializer(album).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, album_id=None):
        if album_id:
            photos = Photos.objects.filter(album_id=album_id, album__owner=request.user)
        else:
            photos = Photos.objects.filter(owner=request.user)
        serializer = PhotosSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request, album_id=None):
        if not album_id:
            return Response({'error': 'Album ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        album = Albums.objects.get(pk=album_id, owner=request.user)
        serializer = PhotosSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(owner=request.user, album=album)
            return Response(PhotosSerializer(photo).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        photo = Photos.objects.get(pk=pk)
        if photo.owner != request.user:
            return Response({'error': 'You are not authorized to update this photo.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = PhotosSerializer(photo, data=request.data)
        if serializer.is_valid():
            photo = serializer.save()
            return Response(PhotosSerializer(photo).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        photo = Photos.objects.get(pk=pk)
        if photo.owner != request.user:
            return Response({'error': 'You are not authorized to delete this photo.'}, status=status.HTTP_403_FORBIDDEN)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


