from .views import *
from django.urls import path,include

urlpatterns = [
    path('login/', LoginView.as_view(),name="login"),
    path("signup/",SignupView.as_view(),name="signup"),
    path("",DashboardTemplateView.as_view(),name="dashboard"),
    
]
