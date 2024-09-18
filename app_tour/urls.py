from django.urls import path
from .views import discount, user


urlpatterns = [
    path('discount/create/', discount.CreateDiscountView.as_view(), name='create_discount'),
    path('discount/list/', discount.ListDiscountView.as_view(), name='list_discount'),
    path('discount/delete/<int:pk>/', discount.DeleteDiscountView.as_view(), name='delete_discount'),
    path('discount/update/<int:pk>/', discount.UpdateDiscountView.as_view(), name='update_discount'),
    path('discount/get/<int:pk>/', discount.RetrieveDiscountView.as_view(), name='get_discount'),
    path('user/create/', user.CreateUserView.as_view(), name='create_user'),
    path('user/list/', user.ListUserView.as_view(), name='list_user'),
    path('user/delete/<int:pk>/', user.DeleteUserView.as_view(), name="delete_user"),
    path('user/update/<int:pk>/', user.UpdateUserView.as_view(), name="update_user"),
    path('user/get/<int:pk>/', user.RetriverUserView.as_view(), name="get_user")

]
