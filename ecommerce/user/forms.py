from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import User
from django import forms

class  UserCreateForm(UserCreationForm):
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
    # phone_no= forms.IntegerField(validators=[RegexValidator(
    #     '[6,7,8,9]{1}[0-9]{9}', message="Enter a Valid Indian Phone Number")])

    class Meta:
        model=User
        fields=['first_name', 'last_name','email', "password1", "password2"]

    
    def save(self):
        email=self.cleaned_data['email']
        first_name=self.cleaned_data['first_name']
        last_name=self.cleaned_data['last_name']
        user=User.objects.create(
            username = email,
            email=email,
            first_name=first_name,
            last_name=last_name,
   
            )
        user.set_password(self.cleaned_data["password1"])
        user.save()        
        return user
    