from django.conf.urls import url,patterns,include
from django.contrib import admin

urlpatterns=patterns('',
(r'^posts/',include('socialapp.urls')),
url(r'^admin/', include(admin.site.urls)),
url(r'^accounts/login/$','socialapp.views.login'),
url(r'^accounts/auth/$','socialapp.views.auth_view'),
url(r'^accounts/logout/$','socialapp.views.logout'),
url(r'^accounts/loggedin/$','socialapp.views.loggedin'),
url(r'^accounts/login/$','socialapp.views.login'),
url(r'^accounts/invalid/$','socialapp.views.invalid_login'),
)
