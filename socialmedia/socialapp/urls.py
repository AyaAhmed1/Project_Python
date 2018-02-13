from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/$',views.dashboard),
    url(r'^allusers/$', views.allusers),
    url(r'(?P<usr_id>[0-9]+)/block',views.block),
    url(r'(?P<usr_id>[0-9]+)/unblock', views.unblock),

    # url(r'^(?P<st_id>[0-9]+$)',views.getstudent),
    # url('^new',views.newStudent),
    # url(r'(?P<st_id>[0-9]+)/update',views.update),
    # url(r'(?P<st_id>[0-9]+)/delete',views.delete)

]