from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    bio = models.TextField()
    phone_number = models.CharField(max_length =15, blank = True)
    prof_photo = models.ImageField(upload_to = 'pics/profiles/')

    def __str__(self):
        return self.name
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
    
    def update_profile(self):
        pass

class Category(models.Model):
    tag = models.CharField(max_length = 30)

    def __str__(self):
        return self.tag

class Comments(models.Model):
    comment = models.CharField(max_length = 500)

    def __str__(self):
        return self.comment

class Image(models.Model):
    image = models.ImageField(upload_to = 'pics/')
    img_name = models.CharField(max_length = 150)
    img_caption = models.CharField(max_length = 1000)
    profile = models.ForeignKey(Profile , on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    comments = models.ManyToManyField(Comments, blank=True)

    def __str__(self):
        return self.image
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def update_image(self):
        pass
