from rest_framework import serializers
from .models import Albums, Photos


class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = ['id', 'name', 'description', 'image', 'is_public', 'owner']
        read_only_fields = ['id', 'owner']


class PhotosSerializer(serializers.ModelSerializer):
    album_name = serializers.CharField(source='album.name', read_only=True)
    
    class Meta:
        model = Photos
        fields = ['id', 'name', 'description', 'image', 'is_public', 'owner', 'album', 'album_name']
        read_only_fields = ['id', 'owner']
