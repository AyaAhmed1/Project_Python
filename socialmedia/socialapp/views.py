# from django.shortcuts import render
# from django.http import HttpResponse
# from django.shortcuts import render_to_response
# from socialapp.models import Posts
# # Create your views here.

# def posts(request):
# 	language='en-gb'
# 	session_language='en-gb'

# 	if 'lang' in request.COOKIES:
# 		language=request.COOKIES['lang']
# 	if 'lang' in request.session:
# 		session_language=request.session['lang']
# 	return render_to_response('posts.html',
# 		{'posts':Posts.objects.all(),
# 		 'language':language,
# 		 'session_language':session_language,
# 		})
# def post(request,post_id=1):
# 	return render_to_response('post.html',
# 		{'post':Posts.objects.get(id=post_id)})	

# def language(request,language='en-gb'):
# 	response=HttpResponse("setting language to %s" % language)
# 	response.set_cookie('lang',language)
# 	request.session['lang']=language
# 	return response
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf


def login(request):
	c={}
	c.update(csrf(request))
	return render_to_response('login.html',c)

def auth_view(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	user=auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		HttpResponse(user)
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render_to_response('loggedin.html',
		                     {'full_name':request.user.username})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')	
