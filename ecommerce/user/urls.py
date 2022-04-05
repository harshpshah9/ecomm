from .views import *
from django.urls import path,include
from product.views import DashboardTemplateView
urlpatterns = [
    path('login/', LoginView.as_view(),name="login"),
    path("signup/",SignupView.as_view(),name="signup"),
    path("home",DashboardTemplateView.as_view(),name="dashboard"),
    
]
