from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import discount, user, rating, visit_history, place


router = DefaultRouter()
router.register(r'discounts', discount.DiscountViewSet, basename='discount')
router.register(r'places', place.PlaceViewSet, basename='place')
router.register(r'users', user.UserViewSet, basename="user")
router.register(r'visit_histories', visit_history.VisitHistoryViewSet, basename="visit_history")
router.register(r'ratings', rating.RatingViewSet, basename="rating")

urlpatterns = [
    # path('discount/create/', discount.CreateDiscountView.as_view(), name='create_discount'),
    # path('discount/list/', discount.ListDiscountView.as_view(), name='list_discount'),
    # path('discount/delete/<int:pk>/', discount.DeleteDiscountView.as_view(), name='delete_discount'),
    # path('discount/update/<int:pk>/', discount.UpdateDiscountView.as_view(), name='update_discount'),
    # path('discount/get/<int:pk>/', discount.RetrieveDiscountView.as_view(), name='get_discount'),
    # path('user/create/', user.CreateUserView.as_view(), name='create_user'),
    # path('user/list/', user.ListUserView.as_view(), name='list_user'),
    # path('user/delete/<int:pk>/', user.DeleteUserView.as_view(), name="delete_user"),
    # path('user/update/<int:pk>/', user.UpdateUserView.as_view(), name="update_user"),
    # path('user/get/<int:pk>/', user.RetriverUserView.as_view(), name="get_user"),
    # path('rating/create/', rating.CreateRatingView.as_view(), name='create_rating'),
    # path('rating/list/', rating.ListRatingView.as_view(), name='list_rating'),
    # path('rating/delete/<int:pk>/', rating.DeleteRatingView.as_view(), name='delete_rating'),
    # path('rating/get/<int:pk>/', rating.RetrieveRatingView.as_view(), name='get_rating'),
    # path('visitHistory/create/', visit_history.CreateVisitHistoryView.as_view(), name='create_visit_history'),
    # path('visitHistory/list/', visit_history.ListVisitHistoryView.as_view(), name='list_visit_history'),
    # path('visitHistory/delete/', visit_history.DeleteVisitHistoryView.as_view(), name='delete_visit_history'),
    # path('visitHistory/update/', visit_history.UpdateVisitHistoryView.as_view(), name='update_visit_history'),
    # path('visitHistory/get/', visit_history.RetrieveVisitHistoryView.as_view(), name='get_visit_history'),
    # path('place/create/', place.CreatePlaceView.as_view(), name='create_place'),
    # path('place/list/', place.ListPlaceView.as_view(), name='list_place'),
    # path('place/delete/', place.DeletePlaceView.as_view(), name='delete_place'),
    # path('place/update/', place.UpdatePlaceView.as_view(), name='update_place'),
    # path('place/get/', place.RetrievePlaceView.as_view(), name='get_place'),
] + router.urls
