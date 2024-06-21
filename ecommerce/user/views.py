from django.shortcuts import redirect,render
from django.contrib.auth.views import LoginView
from base.views import *
from .forms import *
from django.urls.base import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth.views import *


# Create your views here.
class LoginView(LoginView):
    template_name = 'userportal/login.html'
    form_class = LoginForm

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy('custadmin:admin_dashboard')
        else:
            return reverse_lazy('user:dashboard')


class SignupView(BaseCreateView):
    form_class = UserCreateForm
    template_name = "userportal/reg.html"
    success_url = reverse_lazy('user:login')


class WishlistCreateview(LoginRequiredMixin, BaseCreateView):
    def post(self, request, *args, **kwargs):

        product_id = self.kwargs.get('productid')
        product = Product.objects.get(id=product_id)

        wishlist, is_created = Wishlist.objects.get_or_create(user=self.request.user, products=product)
        if is_created:
            wishlist.save()
            message = "wishlist created successfully"
        else:
            wishlist.delete()
            message = "wishlist Remove"
        return JsonResponse(data={
            'message': message
        })


class WishlistListView(LoginRequiredMixin, BaseListView):
    model = Wishlist
    template_name = 'userportal/wistlist.html'
    context_object_name = 'userwistlist'

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)


class WishlistDeleteView(BaseDeleteView):
    model = Wishlist
    template_name = 'userportal/wistlist.html'
    success_url = reverse_lazy('user:wishlist')


class UserProfileUpdateView(BaseUpdateView):
    template_name = 'userportal/userprofile.html'
    model = User
    field = '__all__'
    success_url = reverse_lazy('index')


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ['adminportol/change_password.html']
        else:
            return ['userportal/change_password.html']

class UserAddressCreateView(BaseCreateView):
    model=UserAddress
    fields=['address','state','city','country','zipcode']
    template_name='userportal/address.html'
    def get_success_url(self):
        return reverse_lazy('cart:checkout')
    def form_valid(self, form):
        instance = form.instance
        instance.user = self.request.user
        instance.save()    
        return redirect(self.get_success_url())
               

class UserAddressUpdateview(BaseUpdateView):
    model=UserAddress
    form_class= UserAddressForm
    template_name='userportal/address.html'      
    success_url=reverse_lazy('cart:checkout')

class UserAddressDeleteview(BaseDeleteView):
    model=UserAddress
    template_name='userportal/address.html'
    success_url=reverse_lazy('cart:checkout')


