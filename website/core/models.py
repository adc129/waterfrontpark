from audioop import reverse
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog-details', args=(str(self.id)))
