from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth.models import User

# Create your views here.

def signUp(request):
	user_form=RegistrationForm()
	if request.method=="POST":
		user_form=RegistrationForm(request.POST)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect("/socialapp/signup/")
	context={"form":user_form}
	return render(request,"user/new.html",context)
