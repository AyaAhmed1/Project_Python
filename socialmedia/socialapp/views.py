from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from models import Posts
from models import Comment
from .models import Posts,CateUsr,Like,Dislike


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


def blocked(request):
    return render_to_response('pages/blocked.html')




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
            post_form = Postform(request.POST, instance=post)
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

def home(request):
    user=request.user
    if user.is_active==1:
        all_categories =Category.objects.all()
        cat_subscribtion_arr=[]
        for catObj in all_categories:
            isSub=isSubscriped(catObj.id,user.id)
            subDic= {'cat_id':catObj.id ,"cat_name":catObj.category_name ,'isSubscriped': isSub}
            cat_subscribtion_arr.append(subDic)

        post_list = Posts.objects.order_by('-id')
        page = request.GET.get('page', 1)

        paginator = Paginator(post_list, 2)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        subCategory=CateUsr.objects.filter(user_id=user.id)
        context= {"all_categories":all_categories,"posts":posts,"is_admin":request.user.is_superuser,"full_name":request.user.username,"subCategory":subCategory,"cat_subscribtion_arr":cat_subscribtion_arr}
        return render(request, "pages/home.html" , context)
    else :
        return render_to_response('pages/blocked.html')







def allCategories(request):
    all_categories =Category.objects.all()
    top_posts=Posts.objects.order_by('time')
    context= {"all_categories":all_categories,"all_posts":top_posts,"is_admin":request.user.is_superuser}
    return render(request, "pages/all_cat.html" , context)

def Category_posts(request,cat_id):
    all_Category_posts=Posts.objects.filter(cat_name_id=cat_id).order_by('-id')
    cat_name=Category.objects.get(id=cat_id)
    all_categories =Category.objects.all()
    context={"all_category_posts" :all_Category_posts,"cat_name": cat_name,"all_categories":all_categories ,"is_admin":request.user.is_superuser}
    return render (request,"pages/cat_posts.html",context)

def isSubscriped(cat_id,user_id):
    userSub = CateUsr.objects.filter(user_id=user_id,categ_id=cat_id)
    count=userSub.count()
    if count > 0:
        return True
    else:
        return False


def Post_Page(request, post_id):
    post = Posts.objects.filter(id=post_id)
    all_comments = Comment.objects.order_by('-time').filter(id_post_id=post_id)
    all_users = User.objects.all()
    all_categories = Category.objects.all()
    words = Unwanted.objects.all()
    replys = Reply.objects.all()
    replys = checkReply(words, replys)
    all_comments = check(words, all_comments)
    context = {"post_data": post, "all_categories": all_categories, "allcomments": all_comments, "allusers": all_users,
               'all_replys': replys,"is_admin":request.user.is_superuser}
    return render(request, "pages/post_page.html", context)



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
    context={"Posts_match_title" :Posts_match_title ,"Posts_match_tag":Posts_match_tag,"all_categories":all_categories,"is_admin":request.user.is_superuser}
    return render (request,"pages/filter.html",context)

#alaa
def like_post(request,post_id):
    user=request.user
    like=Like(post_id=post_id,user_id=user.id,status="True")
    a=Like.objects.all()
    for rows in a:
        if(rows.user_id==like.user_id and int(rows.post_id)==int(like.post_id)):
            if(rows.status==1):
                rows.delete()
                like.status=0
            else:
                rows.delete()
                like.status=1
    like.save()  
    dislike=Dislike(post_id=post_id,user_id=user.id,status="True")
    b=Dislike.objects.all()
    for rows in b:
        if(rows.user_id==dislike.user_id and int(rows.post_id)==int(dislike.post_id)):
            if(rows.status==1):
                rows.delete()
                dislike.status=0
            else:
                rows.delete()
                dislike.status=0
    dislike.save()  
    countStatus=b.filter(status=1).count()
    if(countStatus==10):
        post.delete()
    Posts.objects.filter(id=post_id).update(countdislike=countStatus)  

    countStatus=a.filter(status=1).count()
    Posts.objects.filter(id=post_id).update(countlike=countStatus)  
    return HttpResponseRedirect('/socialapp/%s/post_page/'%post_id)

def dislike_post(request,post_id):
    user=request.user
    post = Posts.objects.get(id = post_id)
    dislike=Dislike(post_id=post_id,user_id=user.id,status="True")
    a=Dislike.objects.all()
    for rows in a:
        if(rows.user_id==dislike.user_id and int(rows.post_id)==int(dislike.post_id)):
            if(rows.status==1):
                rows.delete()
                dislike.status=0
            else:
                rows.delete()
                dislike.status=1
    dislike.save()  
    like=Like(post_id=post_id,user_id=user.id,status="True")
    b=Like.objects.all()
    for rows in b:
        if(rows.user_id==like.user_id and int(rows.post_id)==int(like.post_id)):
                if(rows.status==1):
                    rows.delete()
                    like.status=0
                else:
                    rows.delete()
                    like.status=0
    like.save()  
    countStatus=b.filter(status=1).count()
    Posts.objects.filter(id=post_id).update(countlike=countStatus)  
    countStatus=a.filter(status=1).count()
    if(countStatus==10):
        post.delete()
    Posts.objects.filter(id=post_id).update(countdislike=countStatus)  

    return HttpResponseRedirect('/socialapp/%s/post_page/'%post_id)


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
    category = Category.objects.get(id = cat_id)
    user = request.user
    category.users.remove(user)

    CateUsr.objects.filter(categ_id=cat_id,user_id=user.id).delete()
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
        return HttpResponseRedirect('/socialapp/home/')
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

#ghada
@csrf_exempt
def add_like(request, post_id):
    if request.method == 'POST':
        userCount = Like.objects.filter(user_id=request.user.id,post_id=post_id).count()
        userCountD = Dislike.objects.filter(user_id=request.user.id,post_id=post_id).count()


        post1=Posts.objects.get(id=post_id)

        print userCount
        if userCount == 0:
            like = Like.objects.create( post_id=post_id, user_id=request.user.id,status = 1)
            post1.countlike = post1.countlike + 1
            # post1.save()
            if userCountD > 0:
                D = Dislike.objects.get(user_id=request.user.id,post_id=post_id)
                D.delete()
                post1.countdislike = post1.countdislike - 1
            post1.save()


        

        data = {'success': True, 'count': post1.countlike, 'countD' : post1.countdislike
                }
        return JsonResponse(data)

@csrf_exempt
def add_dislike(request, post_id):
     if request.method == 'POST':
        userCount = Dislike.objects.filter(user_id=request.user.id,post_id=post_id).count()
        userCountL = Like.objects.filter(user_id=request.user.id,post_id=post_id).count()

        post1=Posts.objects.get( id=post_id )

        print userCount
        if userCount == 0:
            dislike = Dislike.objects.create( post_id=post_id, user_id=request.user.id,status = 1)
            post1.countdislike = post1.countdislike + 1
            if userCountL > 0:
                L = Like.objects.get(user_id=request.user.id,post_id=post_id)
                L.delete()
                post1.countlike = post1.countlike - 1
            post1.save()
        

        data = {'success': True, 'count': post1.countdislike ,'countL' : post1.countlike
                }
        return JsonResponse(data)






def signUp(request):
    user_form = RegistrationForm()
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect("/socialapp/home/")
    context = {"form": user_form}
    return render(request, "user/new.html", context)


@csrf_exempt
def add_comment(request, post_id):
    if request.method == 'POST':
        com_body = request.POST.get("comment", None)
        comment = Comment.objects.create(c_body=com_body, id_post_id=post_id, c_user_id=1, time=datetime.datetime.now())
        words = Unwanted.objects.all()
        com_body = checkStr(words, com_body)
        # user = "yy"
        data = {'success': True, 'user_name': request.user.username, 'time': datetime.datetime.now(), 'comment': com_body,
                'com_id': comment.id}
        return JsonResponse(data)


@csrf_exempt
def add_reply(request, post_id):
    if request.method == 'POST':
        reply_body = request.POST.get("reply", None)
        comm_id = request.POST.get("comment_id", None)
        reply = Reply.objects.create(R_body=reply_body, post_id_id=comm_id, R_user_id=1,
                                     time_reply=datetime.datetime.now())
        reply.save()
        comment = Comment.objects.get(id=comm_id)
        comment.R_check = 1
        comment.save()
        words = Unwanted.objects.all()
        reply_body = checkStr(words, reply_body)
        # user = "kkk"
        data = {'success': True, 'user_name': request.user.username, 'time': datetime.datetime.now(), 'reply': reply_body}
        return JsonResponse(data)


def check(words, comments):
    for comment in comments:
        for word in words:
            if word.word in comment.c_body:
                star = "*" * len(word.word)
                comment.c_body = comment.c_body.replace(word.word, star)

    return comments


def checkReply(words, replys):
    for reply in replys:
        for word in words:
            if word.word in reply.R_body:
                star = "*" * len(word.word)
                reply.R_body = reply.R_body.replace(word.word, star)

    return replys


def checkStr(words, str_text):
    for word in words:
        if word.word in str_text:
            star = "*" * len(word.word)
            str_text = str_text.replace(word.word, star)
    return str_text




