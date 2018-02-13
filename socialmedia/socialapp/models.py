from django.db import models

class Users(models.Model):
    username = models.CharField(max_length = 50)
    password = models.IntegerField()
    email = models.CharField(max_length = 50)
    is_admin = models.IntegerField()
    is_blocked = models.IntegerField()

class Category(models.Model):
    category_name = models.CharField(max_length = 50)


class Posts(models.Model):
    img = models.CharField(max_length = 255)
    p_body = models.CharField(max_length = 255)
    like = models.IntegerField()
    dislike = models.IntegerField()
    title = models.CharField(max_length = 50)
    tag = models.CharField(max_length = 50)
    cat_name = models.ForeignKey(Category)





