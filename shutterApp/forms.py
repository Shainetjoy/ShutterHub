from django.contrib.auth.forms import UserCreationForm
from django import forms
from shutterApp.models import  User ,Customer



class UserRgistration(UserCreationForm):
    username = forms.CharField()
    password1 =forms.CharField(label='password',widget=forms.PasswordInput)
    password2 =forms.CharField(label='password',widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username','password1','password2')



class CustomerREgistration(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ("user",)

