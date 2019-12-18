from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

    

class Location(models.Model):
    country = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.country
    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()
        
    @classmethod
    def update(cls,id,name):
        location = Location.objects.filter(id=id)
        location.update(country=name)
        return location
    
    

class Category(models.Model):
    category = models.CharField(max_length = 40)
    
    def __str__(self):
        return self.category
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()
    @classmethod
    def update(cls,id,name):
        category = Category.objects.filter(id=id)
        category.update(Category=name)
        return category
    
    
class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category_key = models.ForeignKey(Category,db_column='category')
    pub_date = models.DateTimeField(auto_now_add=True)
    image = ImageField(blank=True, manual_crop="")
    
    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category_key__category__icontains=search_term)
        return image
    
    def __str__(self):
        return self.name
    
    
    
    


    