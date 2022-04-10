from .views import *
from django.urls import path, include
from product.views import DashboardTemplateView, ProductListView

app_name = 'user'
urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("", DashboardTemplateView.as_view(), name="dashboard"),
    path("category/", ProductListView.as_view(), name="category"),
    path('wishlist/<int:productid>', WishlistCreateview.as_view(), name='wishlist_create'),
    path('wishlist/', WishlistListView.as_view(), name='wishlist'),
    path('wistlist/delete/<int:pk>', WishlistDeleteView.as_view(), name='wishlist_delete'),
    path('profile/<int:pk>', UserProfileUpdateView.as_view(), name='profile'),
    path('password/change/ ', PasswordChangeView.as_view(), name="change_password"),

]
