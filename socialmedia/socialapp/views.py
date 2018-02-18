from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from models import Posts
from models import Comment
from models import Category
from models import Unwanted



from form import Userform
from form import Postform
from form import Catform
from form import Wordform


from form import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import datetime
from django.utils.timezone import utc
from models import Unwanted
from models import Reply


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
    all_comments=Comment.objects.order_by('-time').filter(id_post_id=post_id)
    all_users=User.objects.all()
    all_categories =Category.objects.all()
    words=Unwanted.objects.all()
    replys=Reply.objects.all()
    replys=checkReply(words,replys)
    all_comments=check(words,all_comments)
    context={"post_data" : post, "all_categories" :all_categories,"allcomments":all_comments,"allusers":all_users,'all_replys':replys}
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

def signUp(request):
	user_form=RegistrationForm()
	if request.method=="POST":
		user_form=RegistrationForm(request.POST)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect("/socialapp/home/")
	context={"form":user_form}
	return render(request,"user/new.html",context)
@csrf_exempt
def add_comment(request,post_id):
    if request.method =='POST':
        com_body=request.POST.get("comment",None)
        comment=Comment.objects.create(c_body=com_body,id_post_id=post_id,c_user_id=1,time=datetime.datetime.now())
        words=Unwanted.objects.all()  
        com_body=checkStr(words,com_body)   	   
	user="yy"
        data={'success':True,'user_name':user,'time':datetime.datetime.now(),'comment':com_body,'com_id':comment.id}
        return JsonResponse(data)

@csrf_exempt
def add_reply(request,post_id):
    if request.method =='POST':
        reply_body=request.POST.get("reply",None)
        comm_id=request.POST.get("comment_id",None)
        reply=Reply.objects.create(R_body=reply_body,post_id_id=comm_id,R_user_id=1,time_reply=datetime.datetime.now())
        reply.save()
        comment=Comment.objects.get(id=comm_id)
        comment.R_check=1
        comment.save()
        words=Unwanted.objects.all()
        reply_body=checkStr(words,reply_body)      	   
	user="kkk"
        data={'success':True,'user_name':user,'time':datetime.datetime.now(),'reply':reply_body}
        return JsonResponse(data)

def check(words,comments):
   for comment in comments:
	for word in words:
		if word.word in comment.c_body:
			star="*"*len(word.word)
			comment.c_body=comment.c_body.replace(word.word,star)
		
   return comments

def checkReply(words,replys):
   for reply in replys:
	for word in words:
		if word.word in reply.R_body:
			star="*"*len(word.word)
			reply.R_body=reply.R_body.replace(word.word,star)
		
   return replys

def checkStr(words,str_text):
    for word in words:
        if word.word in str_text:
             star="*"*len(word.word)
             str_text=str_text.replace(word.word,star)
    return str_text
















    


