from django.db import models
from cloudinary.models import CloudinaryField

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image = CloudinaryField('image')
    image_location = models.ForeignKey('Location',on_delete=models.CASCADE)
    image_category = models.ForeignKey('Category',on_delete=models.CASCADE)


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self, Name=None, category=None):
        self.image_name = Name if Name else self.Name
        self.image_category = category if category else self.image_category 
        self.save()


    def __str__(self):
        return self.image_name

