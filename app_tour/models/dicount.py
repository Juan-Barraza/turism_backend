from django.db import models
from .place import Place

class Discount(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField()
    
    def __str__(self):
        return f'discount: {self.discount_percentage}, description: {self.description}'