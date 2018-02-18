from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/$',views.dashboard),
    url(r'^allusers/$', views.allusers),
    url(r'(?P<usr_id>[0-9]+)/block',views.block),
    url(r'(?P<usr_id>[0-9]+)/unblock', views.unblock),
    url(r'(?P<usr_id>[0-9]+)/promote', views.promote),
    url(r'(?P<usr_id>[0-9]+)/update', views.update),

    url(r'^allposts/$', views.allposts),
    url(r'^newpost/$', views.newPost),
    url(r'(?P<pst_id>[0-9]+)/deletepst', views.deletepst),
    url(r'(?P<pst_id>[0-9]+)/pstupdate', views.updatepst),

    url(r'^allcat/$', views.allcat),
    url(r'^newcat/$', views.newcat),
    url(r'(?P<cat_id>[0-9]+)/catupdate', views.catupdate),
    url(r'(?P<cat_id>[0-9]+)/catdelete', views.catdelete),

    url(r'^allwords/$', views.allwords),
    url(r'^newword/$', views.newword),
    url(r'(?P<wrd_id>[0-9]+)/wordupdate', views.wordupate),
    url(r'(?P<wrd_id>[0-9]+)/worddelete', views.worddelete),


    url(r'^(?P<cat_id>[0-9]+)/cat_posts/$', views.Category_posts),
    url(r'^(?P<post_id>[0-9]+)/post_page/$', views.Post_Page),
    url(r'^home/$' , views.home),
    url(r'^signup/$',views.signUp),
    url(r'^(?P<post_id>[0-9]+)/comment/$',views.add_comment),
    url(r'^(?P<post_id>[0-9]+)/reply/$',views.add_reply),

]
