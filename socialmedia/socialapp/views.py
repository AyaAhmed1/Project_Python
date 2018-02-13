from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.models import User
from form import Userform
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