from django.test import TestCase

from apps.gallery.models import Album, Photo

class AlbumModelTest(TestCase):
    def setUp(self):
        self.album = Album.objects.create(name="Test Album", description="Test Album Description", image="albums/test.png", is_public=True)
        
        def test_album_name(self):
            self.assertEqual(self.album.name, "Test Album")
            
        def test_album_description(self):
            self.assertEqual(self.album.description, "Test Album Description")
            
        def test_album_image(self):
            self.assertEqual(self.album.image, "albums/test.png")
            
        def test_album_is_public(self):
            self.assertEqual(self.album.is_public, True)
            
class PhotoModelTest(TestCase):
    def setUp(self):
        self.photo = Photo.objects.create(name="Test Photo", description="Test Photo Description", image="photos/test.png", is_public=True)
        
        def test_photo_name(self):
            self.assertEqual(self.photo.name, "Test Photo")
            
        def test_photo_description(self):
            self.assertEqual(self.photo.description, "Test Photo Description")
            
        def test_photo_image(self):
            self.assertEqual(self.photo.image, "photos/test.png")
            
        def test_photo_is_public(self):
            self.assertEqual(self.photo.is_public, True)