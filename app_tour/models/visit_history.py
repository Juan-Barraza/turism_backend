from django.db import models
from .place import Place
from .user import User


class Visit_history(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visit_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'places visit: {self.place}, user: {self.user}, date: {self.visit_date}'