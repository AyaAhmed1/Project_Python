from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    category_name = models.CharField(max_length = 50)
    def __str__(self):
        return self.category_name


class Posts(models.Model):
    # img = models.ImageField(blank=True,default='1.jpeg')
    img = models.CharField(max_length = 255)
    p_body = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    title = models.CharField(max_length = 255)
    tag = models.CharField(max_length = 255)
    cat_name = models.ForeignKey(Category)
    time=models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    c_body = models.CharField(max_length = 255)
    c_user = models.ForeignKey(User)
    id_post = models.ForeignKey(Posts)
    time=models.DateTimeField(auto_now_add=True)    


class Reply(models.Model):
    R_body = models.CharField(max_length = 255)
    R_user = models.ForeignKey(User)
    post_id = models.ForeignKey(Comment)

    def __str__(self):
        return self.id

class CateUsr(models.Model):
    user = models.ForeignKey(User)
    categ = models.ForeignKey(Category)

class Unwanted(models.Model):
    word = models.CharField(max_length = 50)






















