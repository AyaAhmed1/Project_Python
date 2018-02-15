from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import Category,Posts


def allCategories(request):
    all_categories =Category.objects.all()
    top_posts=Posts.objects.order_by('time')
    context= {"all_categories":all_categories,"all_posts":top_posts}
    return render(request, "pages/all_cat.html" , context)

def Category_posts(request,cat_id):
    all_Category_posts=Posts.objects.filter(cat_name_id=cat_id)
    cat_name=Category.objects.get(id=cat_id)
    context={"all_category_posts" :all_Category_posts,"cat_name": cat_name}
    return render (request,"pages/cat_posts.html",context)

def Post_Page(request,post_id):
    post=Posts.objects.filter(id=post_id)
    all_categories =Category.objects.all()
    context={"post_data" : post, "all_categories" :all_categories}
    return render (request,"pages/post_page.html",context)

def home(request):
    all_categories =Category.objects.all()
    post_list = Posts.objects.order_by('time')
    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context= {"all_categories":all_categories,"posts":posts}
    return render(request, "pages/home.html" , context)
