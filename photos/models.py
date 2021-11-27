from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image = CloudinaryField('image')
    image_location = models.ForeignKey('Location',on_delete=models.CASCADE)
    image_category = models.ForeignKey('Category',on_delete=models.CASCADE)
