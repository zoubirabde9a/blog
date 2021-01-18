from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        output_size = (img.width, img.height) 
        if output_size[0] > 300:
           output_size[0] = 300
        if output_size[1] > 300:
           output_size[1] = 300

        img.thumbnail(output_size)
        img.save(self.image.path)
        

# Create your models here.
