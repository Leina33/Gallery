from django.test import TestCase
from .models import Image,Location,Category


        
class LocationTestClass(TestCase):
    def setUp(self):
        self.kisumu=location(place='lakeside')
    
    def_test_save_location(self):
        self.kisumu.save_location().objects.all()
        self.assertTrue(len(location)> 0)


class CategoryTestClass(TestCase:
    def setUp(self):
        self.tour=Category(name='parties'):
            
    def_test_save_location(self):
        self.tour.save=category()
        categories = category.objects.all()
        self.assertTrue(len(categories) > 0)
        
        
        #tests
        
    self.kisumu=location(place='lakeside')
    self.tour=category(name='parties')
    self.kisumu.save_location()
    self.tour.save_category()
    
    self.bash = Image(image_name ='party',image_description ='happy moments',image_location=self.kisumu,image_category=self.tour)
    
    