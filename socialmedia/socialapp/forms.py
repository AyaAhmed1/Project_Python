import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(UserCreationForm):

	username=forms.CharField(label='Username',max_length=30)
	email=forms.EmailField(label='Email')
	class Meta:
		model=User
		fields=('username','email',)

	def clean_username(self):
		username=self.cleaned_data['username']
		if not re.search(r'^\w+$',username):
			raise forms.ValidationError('username can only contain alphanumeric characters and the underscore.')
		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError('username is already taken.')		

	def clean_email(self):
		email=self.cleaned_data['email']
		try:
			User.objects.get(email=email)
		except ObjectDoesNotExist:
			return email
		raise forms.ValidationError('email is already taken.')







