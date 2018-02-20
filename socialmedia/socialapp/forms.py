
from django import forms
from django import forms


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms.widgets import Widget
from django.contrib.auth.forms import  UserCreationForm


class UserRegisterForm (forms.ModelForm):
    email= forms.EmailField(label='Email address')
    email2= forms.EmailField(label='confirm Email')
    password=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput , label='Confirm password')
    username=forms.CharField(label='user name')

    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'email2',
                  'password' ,
                  'password2']

        widgets = {
             'username': forms.TextInput(attrs={'class': 'form-control '}),
             'email': forms.Textarea(attrs={'class': 'form-control '}),
             'email2': forms.TextInput(attrs={"type": 'file'}),
             'password': forms.Select(attrs={'class': 'form-control '}),
             'password2': forms.Select(attrs={"type": 'file'}),
         }


    def clean(self,*args,**kwargs):
        #print(self.cleaned_data)
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        print(password,password2)
        if password != password2:
            raise forms.ValidationError("Passwords didn't matched !!")

        print(email,email2)
        if email != email2:
            raise forms.ValidationError("Emails didn't matched !")


        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("this email is already registered")

    #    username_qs = User.objects.filter(username=username)
    #    if username_qs.exists():
    #        raise forms.ValidationError("this user name is already registered")


        return super (UserRegisterForm,self).clean(*args , **kwargs)

    def clean_email2 (self):
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        print(password,password2)
        if password != password2:
            raise forms.ValidationError("Passwords didn't matched !")


        print(email,email2)
        if email != email2:
            raise forms.ValidationError("Emails didn't matched !")


        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("this email is already registered")
        return email

    



        
