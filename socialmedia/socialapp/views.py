from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Category


def allCategories(request):
    all_categories =Category.objects.all()
    context= {"all_categories":all_categories}
    return render(request, "pages/all_cat.html" , context)
