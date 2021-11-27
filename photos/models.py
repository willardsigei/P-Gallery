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

    @classmethod
    def search_by_image_category(cls,search_term):
        images = cls.objects.filter(image_category__category_name__icontains=search_term)
        return images
    @classmethod
    def images(cls):
        images = cls.objects.all()
        return images 

    @classmethod
    def filterimageByLocation(cls,location):
        location = cls.objects.filter(image_location__location_name = location).all()
        return location    

class Category(models.Model):
    category_name = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.category_name


class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.location_name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(location_name=value)

