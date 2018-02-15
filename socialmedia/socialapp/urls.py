from django.conf.urls import url,patterns,include
from django.contrib import admin


urlpatterns = patterns('', 
    url(r'^admin/', admin.site.urls),
    #url(r'^all/$','socialapp.views.posts'),
	#url(r'^get/(?P<post_id>\d+)/$','socialapp.views.post'),
	#url(r'^language/(?P<language>[a-z\-]+)/$','socialapp.views.language'),
    )
