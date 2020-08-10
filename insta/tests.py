from django.test import TestCase

from .models import Image, Category, Comments, Profile

# Create your tests here.
class ImageTestClass:
    def setUp(self):
        self.img = Image(image = "https://en.wikipedia.org/wiki/File:Image_created_with_a_mobile_phone.png", img_name = "Wikipedia", img_caption = "An image from Wikipedia", likes = 10)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.img, Image))
    
    def test_save_method(self):
        self.img.save_image()
        imgs = Image.objects.all()
        self.assertTrue(len(imgs) > 0)

class ProfileTestClass:
    pass

class CommentsTestClass:
    pass

class CategoryTestClass:
    pass
