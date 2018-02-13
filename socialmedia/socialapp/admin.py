from django.contrib import admin
from .models import User,Category,Posts ,Comment , Reply, CateUsr,Unwanted


admin.site.register(Posts)

admin.site.register(Category)

admin.site.register(Comment)

admin.site.register(Reply)

admin.site.register(CateUsr)

admin.site.register(Unwanted)





