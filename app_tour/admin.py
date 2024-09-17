from django.contrib import admin
from .models import User, Place, Rating, Discount, Visit_history


admin.site.register(User)
admin.site.register(Place)
admin.site.register(Discount)
admin.site.register(Rating)
admin.site.register(Visit_history)

