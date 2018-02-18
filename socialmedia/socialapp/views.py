from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from models import Posts
from models import Category
from models import Unwanted
from django.db.models import Q

def dashboard(request):
    return render(request,'pages/dashboard.html')

def allusers(request):
    all_users = User.objects.all()
    context = {'allusers': all_users}
    return render(request, 'pages/all_user.html', context)

def block(request,usr_id):
    user=User.objects.get(id=usr_id)
    user.is_active = 0
    user.save()
    return HttpResponseRedirect("/socialapp/allusers")

def unblock(request,usr_id):
    user=User.objects.get(id=usr_id)
    user.is_active = 1
    user.save()
    return HttpResponseRedirect("/socialapp/allusers")

def promote(request,usr_id):
    user=User.objects.get(id=usr_id)
    user.is_superuser = 1
    user.save()
    return HttpResponseRedirect("/socialapp/allusers")

def update (request,usr_id):
    user=User.objects.get(id=usr_id)
    user_form=Userform(instance=user)
    if request.method=="POST":
        user_form = Userform(request.POST,instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect("/socialapp/allusers")
    context = {"form": user_form}
    return render(request, 'pages/update.html', context)

#posts part

def allposts(request):
    all_posts = Posts.objects.order_by('-id')
    context = {'allposts': all_posts}
    return render(request, 'pages/all_posts.html', context)

def deletepst(request,pst_id):
    post=Posts.objects.get(id=pst_id)
    post.delete();
    return HttpResponseRedirect("/socialapp/allposts")

def updatepst (request,pst_id):
    post=Posts.objects.get(id=pst_id)
    post_form=Postform(instance=post)
    if request.method=="POST":
        post_form = Postform(request.POST,instance=post)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect("/socialapp/allposts")
    context = {"form": post_form}
    return render(request, 'pages/updatepst.html', context)

def newPost(request):
    Post_form =Postform()
    if request.method == "POST":
        Post_form=Postform(request.POST)
        if Post_form.is_valid():
            Post_form.save()
            return HttpResponseRedirect('/socialapp/allposts')
    context = {"form" : Post_form}
    return render (request ,'pages/newpost.html',context)


# category part

def allcat(request):
    all_cats = Category.objects.order_by('-id')
    context = {'allcats': all_cats}
    return render(request, 'pages/allcat.html', context)

def newcat (request):
    cat_form = Catform()
    if request.method == "POST":
        cat_form = Catform(request.POST)
        if cat_form.is_valid():
            cat_form.save()
            return HttpResponseRedirect('/socialapp/allcat')
    context = {"form": cat_form}
    return render(request, 'pages/newcat.html', context)

def catupdate (request,cat_id):
    cat=Category.objects.get(id=cat_id)
    cat_form=Catform(instance=cat)
    if request.method=="POST":
        cat_form = Catform(request.POST,instance=cat)
        if cat_form.is_valid():
            cat_form.save()
            return HttpResponseRedirect("/socialapp/allcat")
    context = {"form": cat_form}
    return render(request, 'pages/updatecat.html', context)

def catdelete (request,cat_id):
    cat = Category.objects.get(id=cat_id)
    cat.delete()
    return HttpResponseRedirect("/socialapp/allcat")


#unwanted word

def allwords(request):
    words = Unwanted.objects.order_by('-id')
    context = {'allwords': words}
    return render(request, 'pages/allwords.html', context)

def newword (request):
    word_form = Wordform()
    if request.method == "POST":
        word_form = Wordform(request.POST)
        if word_form.is_valid():
            word_form.save()
            return HttpResponseRedirect('/socialapp/allwords')
    context = {"form": word_form}
    return render(request, 'pages/newword.html', context)

def wordupate(request,wrd_id):
    wrd=Unwanted.objects.get(id=wrd_id)
    word_form=Wordform(instance=wrd)
    if request.method == "POST":
        word_form = Wordform(request.POST,instance=wrd)
        if word_form.is_valid():
            word_form.save()
            return HttpResponseRedirect("/socialapp/allwords")
    context = {"form": word_form}
    return render(request, 'pages/updatewrd.html', context)



def worddelete(request,wrd_id):
    wrd=Unwanted.objects.get(id=wrd_id)
    wrd.delete()
    return HttpResponseRedirect("/socialapp/allwords")


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
    post_list = Posts.objects.order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(post_list,2)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context= {"all_categories":all_categories,"posts":posts}
    return render(request, "pages/home.html" , context)

import json
def get_search(request):
    if request.is_ajax():
        q = request.GET.get('term','')
        query = Q(title__contains=q)
        query.add(Q(tag__contains=q),Q.OR)
        matches =Posts.objects.filter(query)
        results = []
        for post in matches:
            post_json = {}
            post_json['label']= post.title
            post_json['id']=post.id
            results.append(post_json)
            data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def filter(request,keyword):
    Posts_match_title=Posts.objects.filter(title__contains=keyword)
    Posts_match_tag=Posts.objects.filter(tag__contains=keyword)
    all_categories =Category.objects.all()
    context={"Posts_match_title" :Posts_match_title ,"Posts_match_tag":Posts_match_tag,"all_categories":all_categories}
    return render (request,"pages/filter.html",context)
