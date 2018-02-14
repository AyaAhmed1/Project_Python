from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.models import User
from models import Posts
from form import Userform
from form import Postform


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