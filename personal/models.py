from django.db import models

# Create your models here.

    

class Location(models.Model):
    country = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.country
    
    

class Category(models.Model):
    Category = models.CharField(max_length = 40)
    
    def __str__(self):
        return self.Category
    
    
class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    Category = models.ForeignKey(Category,db_column='category')
    
    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(title__icontains=search_term)
        return image
    
    def __str__(self):
        return self.name
    
    


    