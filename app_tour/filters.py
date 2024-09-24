import django_filters
from app_tour.models import Place, Discount, Visit_history, User, Rating

class PlaceFilter(django_filters.FilterSet):
    class Meta:
        model = Place
        fields = {
            'name': ['icontains'],
            'description': ['icontains'],
            'price': ['gte', 'lte'],
            'opening_hours': ['gte', 'lte'],
            'tags': ['icontains'],
        }

class DiscountFilter(django_filters.FilterSet):
    class Meta:
        model = Discount
        fields = {
            'place__name': ['icontains'],
            'description': ['icontains'],
            'discount_percentage': ['gte', 'lte'],
            'start_date':['gte', 'lte'],
            'end_date': ['gte', 'lte'],
        }
    

class RatingFilter(django_filters.FilterSet):
    class Meta:
        model = Rating
        fields = {
            'place__name': ['icontains'],
            'user__first_name': ['icontains'],
            'rating': ['icontains'],
            'rating': ['icontains'],
            'review':['icontains'],
            'date': ['gte', 'lte'],
        }

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'preferred_language': ['icontains'],
            'is_vip': ['icontains'],
        }
        
class VisitHistoryFilter(django_filters.FilterSet):
    class Meta:
        model = Visit_history
        fields = {
            'place__name': ['icontains'],
            'user__first_name': ['icontains'],
            'visit_date': ['gte', 'lte'],
        }