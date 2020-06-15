from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils import timezone
from django.contrib import auth
# Create your models here.


class Post(models.Model): 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    # For Publishing A Post
    def publish(self):
        self.published_date = timezone.now()
        self.save



    # For Approving A Comment
    def approve_comment(self):
        return self.comments.filter(approved_comments=True)


    def get_absolute_url(self):
        return reverse("blog:detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name= 'comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    approved_comments = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)