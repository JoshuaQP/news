from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# we want an Article , that has the following fields:
#title,body,date,author

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add= True)

# Create your models here.
def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse("article_detail", args=[str(self.id)])
