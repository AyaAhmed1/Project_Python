from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^dashboard/$',views.dashboard),
    url(r'^allusers/$', views.allusers),
    url(r'(?P<usr_id>[0-9]+)/block',views.block),
    url(r'(?P<usr_id>[0-9]+)/unblock', views.unblock),
    url(r'(?P<usr_id>[0-9]+)/promote', views.promote),
    url(r'(?P<usr_id>[0-9]+)/unpromote', views.unpromote),

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
    url(r'^noaccess/$', views.noaccess),



    url(r'^(?P<cat_id>[0-9]+)/cat_posts/$', views.Category_posts),
    url(r'^(?P<post_id>[0-9]+)/post_page/$', views.Post_Page),
    url(r'^home/$', views.home),
    url(r'^home/get_search/', views.get_search, name='get_search'),
    url(r'^(?P<id>[0-9]+)/cat_posts/get_search/', views.get_search, name='get_search'),
    url(r'^(?P<keyword>[a-zA-Z]+)/filter/$', views.filter),
    #alaa
    url(r'^like/(?P<post_id>\d+)/$',views.like_post),
	url(r'^dislike/(?P<post_id>\d+)/$',views.dislike_post),
	url(r'^unsubscribe/(?P<cat_id>[0-9]+)/$', views.unsubscribe_category),
	url(r'^subscribe/(?P<cat_id>[0-9]+)/$', views.subscribe_category),
	url(r'^accounts/login/$',views.login),
	url(r'^accounts/auth/$',views.auth_view),
	url(r'^accounts/logout/$',views.logout),
	url(r'^accounts/loggedin/$',views.loggedin),
	url(r'^accounts/login/$',views.login),
	url(r'^accounts/invalid/$',views.invalid_login),

]
