from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Category,Posts


def allCategories(request):
    all_categories =Category.objects.all()
    context= {"all_categories":all_categories}
    return render(request, "pages/all_cat.html" , context)


def Category_posts(request,category_name):
    return HttpResponse("Test")
    # all_Category_posts=Posts.get(cat_name=category_name)
    # context={"all_category_posts" :all_Category_posts}
    # return render (request,"pages/cat_posts",context)
