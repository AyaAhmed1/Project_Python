from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    category_name = models.CharField(max_length = 50)
    def __str__(self):
        return self.category_name
#alaa
    users = models.ManyToManyField(User, null = True ,blank = True)





class Posts(models.Model):
    img = models.ImageField(upload_to='upload' , blank=True)
    p_body = models.TextField()
    title = models.CharField(max_length = 255)
    tag = models.CharField(max_length = 255)
    cat_name = models.ForeignKey(Category)
    time=models.DateTimeField(auto_now_add=True)
    countlike=models.IntegerField(default=0)
    countdislike=models.IntegerField(default=0)


class Comment(models.Model):
    c_body = models.CharField(max_length = 255)
    c_user = models.ForeignKey(User)
    id_post = models.ForeignKey(Posts)
    time=models.DateTimeField()
    #ghada
    R_check=models.IntegerField(default=0)



class Reply(models.Model):
    R_body = models.CharField(max_length = 255)
    R_user = models.ForeignKey(User)
    post_id = models.ForeignKey(Comment)
    time_reply=models.DateTimeField()


    def __str__(self):
        return self.id

class CateUsr(models.Model):
    user = models.ForeignKey(User)
    categ = models.ForeignKey(Category)
    status=models.BooleanField(default=True)#alaa

class Like(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Posts)
    status=models.BooleanField(default=True)

class Dislike(models.Model):
    post = models.ForeignKey(Posts)
    user = models.ForeignKey(User)
    status=models.BooleanField(default=True)


class Unwanted(models.Model):
    word = models.CharField(max_length = 50)






















