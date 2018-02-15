from django import forms
from django.contrib.auth.models import User
from . models import Posts
from . models import Category
from . models import Unwanted



class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields=('username','email')

class Postform(forms.ModelForm):
    class Meta:
        model = Posts
        fields=('img','title','p_body','tag','cat_name')


class Catform(forms.ModelForm):
    class Meta:
        model = Category
        fields=('category_name',)



class Wordform(forms.ModelForm):
    class Meta:
        model = Unwanted
        fields=('word',)