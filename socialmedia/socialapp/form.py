from django import forms
from django.contrib.auth.models import User
from . models import Posts


class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields=('username','email')

class Postform(forms.ModelForm):
    class Meta:
        model = Posts
        fields=('title','p_body','tag','cat_name')