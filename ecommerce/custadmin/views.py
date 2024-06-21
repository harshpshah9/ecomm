from django.shortcuts import render
from base.views import *
from user.models import *
from django.views.generic import TemplateView
# Create your views here.


class AdminDashboard(TemplateView):
    template_name='adminportol/dashboard.html'



class UserListView(BaseListView):
    template_name = 'adminportol/user_list.html'
    queryset = User.objects.filter(is_staff=False)
    model = User
    context_object_name = 'users'
    