from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=255) 
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    longitude =models.DecimalField(max_digits=5, decimal_places=2) 
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    opening_hours = models.CharField(max_length=100) 
    tags = models.TextField()  
    picture = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name

    def set_tags(self, tags_list):
        self.tags = ','.join(tags_list)

    def get_tags(self):
        return self.tags.split(',')
