from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    
    
    def __str__(self):
        return self.name
    

class Location(models.Model):
    country = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.location
    
    


    