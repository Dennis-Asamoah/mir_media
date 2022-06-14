from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import  slugify


class Article(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    content = models.TextField(max_length=900, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    publications_datetime = models.DateTimeField(auto_now_add=True)
    switch = models.BooleanField(default=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class ContactRequest(models.Model):
    email = models.EmailField(max_length=200, null=True, unique=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(max_length=900, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.email

  
    

