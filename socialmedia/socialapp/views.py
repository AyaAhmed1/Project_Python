from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Category,Posts


def allCategories(request):
    all_categories =Category.objects.all()
    top_posts=Posts.objects.all()
    context= {"all_categories":all_categories,"all_posts":top_posts}
    return render(request, "pages/all_cat.html" , context)


def Category_posts(request,cat_id):
    all_Category_posts=Posts.objects.filter(cat_name_id=cat_id)
    cat_name=Category.objects.get(id=cat_id)
    context={"all_category_posts" :all_Category_posts,"cat_name": cat_name}
    return render (request,"pages/cat_posts.html",context)
