from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from models import Posts
from models import Category
from models import Unwanted
from django.db.models import Q
from pprint import pprint
from .models import Category,Posts,CateUsr
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core import mail



from form import Userform
from form import Postform
from form import Catform
from form import Wordform




def dashboard(request):
    if request.user.is_superuser == 1 :
        all_users = User.objects.all()
        all_posts = Posts.objects.order_by('-id')
        words = Unwanted.objects.order_by('-id')
        all_cats = Category.objects.order_by('-id')
        context = {'allusers': all_users ,'allposts': all_posts,'allwords': words,'allcats': all_cats,"is_admin":request.user.is_superuser}
        return render(request,'pages/dashboard.html',context)
    else :
        return HttpResponseRedirect("/socialapp/noaccess")


def allusers(request):
    if request.user.is_superuser == 1 :
        all_users = User.objects.all()
        context = {'allusers': all_users,'bigboss':request.user.id,"is_admin":request.user.is_superuser}
        return render(request, 'pages/all_user.html', context)
    else :
        return HttpResponseRedirect("/socialapp/noaccess")

def block(request,usr_id):
    user=User.objects.get(id=usr_id)
    if request.user.id == 1 :
        user.is_active = 0
        user.save()
        return HttpResponseRedirect("/socialapp/allusers")
    elif request.user.is_superuser == 1 and user.is_superuser == 0:
        user.is_active = 0
        user.save()
        return HttpResponseRedirect("/socialapp/allusers")
    else :
        return HttpResponseRedirect("/socialapp/noaccess")


def unblock(request,usr_id):
    user=User.objects.get(id=usr_id)
    if request.user.id == 1 :
        user.is_active = 1
        user.save()
        return HttpResponseRedirect("/socialapp/allusers")
    elif request.user.is_superuser == 1 and user.is_superuser == 0:
        user.is_active = 1
        user.save()
        return HttpResponseRedirect("/socialapp/allusers")
    else :
        return HttpResponseRedirect("/socialapp/noaccess")



def promote(request,usr_id):
    user=User.objects.get(id=usr_id)
    if request.user.id == 1 :
        user.is_superuser = 1
        user.save()
        return HttpResponseRedirect("/socialapp/allusers")
    elif request.user.is_superuser == 1 and user.is_superuser == 0:
        user.is_superuser = 1
        user.save()
        return HttpResponseRedirect("/socialapp/allusers")
    else :
        return HttpResponseRedirect("/socialapp/noaccess")




def unpromote(request,usr_id):
    user=User.objects.get(id=usr_id)
    if request.user.id == 1 :
        user.is_superuser = 0
        user.save()
        return HttpResponseRedirect("/socialapp/allusers")
    else :
        return HttpResponseRedirect("/socialapp/noaccess")


def noaccess(request):
    return render_to_response('pages/noaccess.html')




def update (request,usr_id):

        user1=User.objects.get(id=usr_id)
        user_form=Userform(instance=user1)
        if request.method=="POST":
            user_form = Userform(request.POST,instance=user1)
            if user_form.is_valid():
                user_form.save()
                return HttpResponseRedirect("/socialapp/allusers")
        context = {"form": user_form,"is_admin":request.user.is_superuser,"who":request.user.id,"id":user1.id,'normaluser':user1.is_superuser}
        return render(request, 'pages/update.html', context)




#posts part

def allposts(request):
    if request.user.is_superuser == 1 :
        all_posts = Posts.objects.order_by('-id')
        context = {'allposts': all_posts,"is_admin":request.user.is_superuser}
        return render(request, 'pages/all_posts.html', context)
    else :
        return render_to_response('pages/noaccess.html')


def deletepst(request,pst_id):
    if request.user.is_superuser == 1 :
        post=Posts.objects.get(id=pst_id)
        post.delete();
        return HttpResponseRedirect("/socialapp/allposts")
    else :
            return render_to_response('pages/noaccess.html')

def updatepst (request,pst_id):
    if request.user.is_superuser == 1 :
        post=Posts.objects.get(id=pst_id)
        post_form=Postform(instance=post)
        if request.method=="POST":
            post_form = Postform(request.POST,instance=post)
            if post_form.is_valid():
                post_form.save()
                return HttpResponseRedirect("/socialapp/allposts")
        context = {"form": post_form,"is_admin":request.user.is_superuser}
        return render(request, 'pages/updatepst.html', context)
    else :
            return render_to_response('pages/noaccess.html')

def newPost(request):
    if request.user.is_superuser == 1 :
        Post_form =Postform()
        if request.method == "POST":
            Post_form=Postform(request.POST, request.FILES)
            if Post_form.is_valid():
                Post_form.save()
                return HttpResponseRedirect('/socialapp/allposts')
        context = {"form" : Post_form,"is_admin":request.user.is_superuser}
        return render (request ,'pages/newpost.html', context)
    else :
            return render_to_response('pages/noaccess.html')


# category part

def allcat(request):
    if request.user.is_superuser == 1 :
        all_cats = Category.objects.order_by('-id')
        context = {'allcats': all_cats,"is_admin":request.user.is_superuser}
        return render(request, 'pages/allcat.html', context)
    else :
            return render_to_response('pages/noaccess.html')

def newcat (request):
    if request.user.is_superuser == 1 :
        cat_form = Catform()
        if request.method == "POST":
            cat_form = Catform(request.POST)
            if cat_form.is_valid():
                cat_form.save()
                return HttpResponseRedirect('/socialapp/allcat')
        context = {"form": cat_form,"is_admin":request.user.is_superuser}
        return render(request, 'pages/newcat.html', context)
    else :
            return render_to_response('pages/noaccess.html')

def catupdate (request,cat_id):
    if request.user.is_superuser == 1 :
        cat=Category.objects.get(id=cat_id)
        cat_form=Catform(instance=cat)
        if request.method=="POST":
            cat_form = Catform(request.POST,instance=cat)
            if cat_form.is_valid():
                cat_form.save()
                return HttpResponseRedirect("/socialapp/allcat")
        context = {"form": cat_form,"is_admin":request.user.is_superuser}
        return render(request, 'pages/updatecat.html', context)
    else :
            return render_to_response('pages/noaccess.html')

def catdelete (request,cat_id):
    if request.user.is_superuser == 1 :
        cat = Category.objects.get(id=cat_id)
        cat.delete()
        return HttpResponseRedirect("/socialapp/allcat")
    else :
        return render_to_response('pages/noaccess.html')


#unwanted word

def allwords(request):
    if request.user.is_superuser == 1 :
        words = Unwanted.objects.order_by('-id')
        context = {'allwords': words,"is_admin":request.user.is_superuser}
        return render(request, 'pages/allwords.html', context)
    else :
        return render_to_response('pages/noaccess.html')

def newword (request):
    if request.user.is_superuser == 1 :
        word_form = Wordform()
        if request.method == "POST":
            word_form = Wordform(request.POST)
            if word_form.is_valid():
                word_form.save()
                return HttpResponseRedirect('/socialapp/allwords')
        context = {"form": word_form,"is_admin":request.user.is_superuser}
        return render(request, 'pages/newword.html', context)
    else :
        return render_to_response('pages/noaccess.html')

def wordupate(request,wrd_id):
    if request.user.is_superuser == 1 :
        wrd=Unwanted.objects.get(id=wrd_id)
        word_form=Wordform(instance=wrd)
        if request.method == "POST":
            word_form = Wordform(request.POST,instance=wrd)
            if word_form.is_valid():
                word_form.save()
                return HttpResponseRedirect("/socialapp/allwords")
        context = {"form": word_form,"is_admin":request.user.is_superuser}
        return render(request, 'pages/updatewrd.html', context)
    else :
        return render_to_response('pages/noaccess.html')



def worddelete(request,wrd_id):
    if request.user.is_superuser == 1 :
        wrd=Unwanted.objects.get(id=wrd_id)
        wrd.delete()
        return HttpResponseRedirect("/socialapp/allwords")
    else :
        return render_to_response('pages/noaccess.html')






def allCategories(request):
    all_categories =Category.objects.all()
    top_posts=Posts.objects.order_by('time')
    context= {"all_categories":all_categories,"all_posts":top_posts,"is_admin":request.user.is_superuser}
    return render(request, "pages/all_cat.html" , context)

def Category_posts(request,cat_id):
    all_Category_posts=Posts.objects.filter(cat_name_id=cat_id)
    cat_name=Category.objects.get(id=cat_id)
    all_categories =Category.objects.all()
    context={"all_category_posts" :all_Category_posts,"cat_name": cat_name,"all_categories":all_categories ,"is_admin":request.user.is_superuser}
    return render (request,"pages/cat_posts.html",context)

def Post_Page(request,post_id):
    post=Posts.objects.filter(id=post_id)
    all_categories =Category.objects.all()
    context={"post_data" : post, "all_categories" :all_categories,"is_admin":request.user.is_superuser}
    return render (request,"pages/post_page.html",context)

def home(request):
    all_categories =Category.objects.all()
    post_list = Posts.objects.order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 2)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context= {"all_categories":all_categories,"posts":posts,"is_admin":request.user.is_superuser}
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

#alaa
def like_post(request, post_id):
    if post_id:
        a = Posts.objects.get(id=post_id)
        a.like.add(request.user)

    return HttpResponseRedirect('/socialapp/%s/post_page/' % post_id)


def dislike_post(request, post_id):
    if post_id:
        a = Posts.objects.get(id=post_id)
        a.dislike.add(request.user)
        count = a.count()
        if (count == 10):
            a.delete()
    return HttpResponseRedirect('/socialapp/%s/post_page/' % post_id)


def subscribe_category(request, cat_id):
    user = request.user
    category = Category.objects.get(id=cat_id)

    cateusr = CateUsr(user_id=user.id, categ_id=cat_id, status="True")
    a = CateUsr.objects.all()

    for rows in a:
        if (rows.user_id == cateusr.user_id and int(rows.categ_id) == int(cateusr.categ_id)):
            if (rows.status == 1):
                rows.delete()
                cateusr.status = 0
            else:
                rows.delete()
                cateusr.status = 1

    cateusr.save()
    category.users.add(user)

    connection = mail.get_connection()
    connection.open()
    msgbodytext = "Hello - " + user.username + "- you have subscribed successfully in - " + category.category_name + " -  SocialApp"
    sendEmail = mail.EmailMessage(
        'Verification',
        msgbodytext,
        'alaametwally48@gmail.com',
        [user.email],
        connection=connection,
    )

    sendEmail.send()
    connection.close()
    return HttpResponseRedirect("/socialapp/home/")


def unsubscribe_category(request, cat_id):
    category = Category.objects.get(id=cat_id)
    user = request.user
    category.users.remove(user)
    return HttpResponseRedirect("/socialapp/home/")


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        request.session.user = user

        return HttpResponseRedirect('/socialapp/accounts/loggedin')
    else:
        HttpResponse(user)
        return HttpResponseRedirect('/socialapp/accounts/invalid')


def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username}
                              )


def invalid_login(request):
    return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
