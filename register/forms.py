from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import BuyBook
from .models import Profile

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

class BuyingForm(forms.ModelForm):
	email = forms.EmailField()
	address = forms.CharField(label="Address")
	phonenumber = forms.IntegerField(label="Phone Number")
	card_no = forms.CharField(label="Card No")
	card_password = forms.IntegerField(label="Card Pin")

	class Meta:
		model = BuyBook
		fields = ["email"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']