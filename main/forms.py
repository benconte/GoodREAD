from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Comments


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ('comments', 'date_added')

		widgets = {
			# 'username':forms.TextInput(attrs={'class':'form-control'}),
			'comment': forms.Textarea(attrs={'class':'form-control'}),
			
		}