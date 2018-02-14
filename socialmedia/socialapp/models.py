from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length = 50,default='')
    def __str__(self):
        return self.category_name


class Posts(models.Model):
    # img = models.ImageField(blank=True,default='1.jpeg')
    img = models.ImageField(blank=True,default='1.jpeg')
    p_body = models.CharField(max_length = 255,default='')
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    title = models.CharField(max_length = 50,default='')
    tag = models.CharField(max_length = 50,default='')
    cat_name = models.ForeignKey(Category)

class Comment(models.Model):
    c_body = models.CharField(max_length = 255,default='')
    c_user = models.ForeignKey(User)
    id_post = models.ForeignKey(Posts)

class Reply(models.Model):
    R_body = models.CharField(max_length = 255,default='')
    R_user = models.ForeignKey(User)
    post_id = models.ForeignKey(Comment)

    def __str__(self):
        return self.id

class CateUsr(models.Model):
    user = models.ForeignKey(User)
    categ = models.ForeignKey(Category)

class Unwanted(models.Model):
    word = models.CharField(max_length = 50,default='')






















