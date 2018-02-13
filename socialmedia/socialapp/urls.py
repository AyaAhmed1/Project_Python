from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^allCategories/$', views.allCategories),
		url(r'^/socialapp/(?P<cat_name>[A-Za-Z0-9]+)/cat_posts/$', views.Category_posts),
		]
