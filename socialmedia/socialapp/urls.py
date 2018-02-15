from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^(?P<cat_id>[0-9]+)/cat_posts/$', views.Category_posts),
	url(r'^(?P<post_id>[0-9]+)/post_page/$', views.Post_Page),
	url(r'^home/$' , views.home),
		]
