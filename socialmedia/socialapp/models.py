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
    img = models.ImageField(upload_to='upload' ,default='1.jpeg', blank=True)
    p_body = models.TextField()
    # like = models.IntegerField(default=0)
    # dislike = models.IntegerField(default=0)
    #alaa
    like = models.ManyToManyField(User, null=True, blank=True, related_name="like")
    dislike = models.ManyToManyField(User, null=True, blank=True, related_name="dislike")

    title = models.CharField(max_length = 255)
    tag = models.CharField(max_length = 255)
    cat_name = models.ForeignKey(Category)
    time=models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    c_body = models.CharField(max_length = 255)
    c_user = models.ForeignKey(User)
    id_post = models.ForeignKey(Posts)
    time=models.DateTimeField()


class Reply(models.Model):
    R_body = models.CharField(max_length = 255)
    R_user = models.ForeignKey(User)
    post_id = models.ForeignKey(Comment)

    def __str__(self):
        return self.id

class CateUsr(models.Model):
    user = models.ForeignKey(User)
    categ = models.ForeignKey(Category)
    status=models.BooleanField(default=True)#alaa


class Unwanted(models.Model):
    word = models.CharField(max_length = 50)






















