from django.db import models

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

class Comment(models.Model):
    c_body = models.CharField(max_length = 255)
    c_user = models.ForeignKey(User)
    id_post = models.ForeignKey(Posts)

class Reply(models.Model):
    R_body = models.CharField(max_length = 255)
    R_user = models.ForeignKey(User)
    post_id = models.ForeignKey(Comment)

class CateUsr(models.Model):
    user = models.ForeignKey(User)
    categ = models.ForeignKey(Category)

class Unwanted(models.Model):
    word = models.CharField(max_length = 50)
