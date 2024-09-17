from django.db import models
from .place import Place
from .user import User


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'rating: {self.rating}'
    