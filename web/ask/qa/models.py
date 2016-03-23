from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Question(models.Model):
    title    = models.CharField(max_length="255")
    text     = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating   = models.IntegerField()
    author   = models.ForeignKey(User)
    likes    = models.ManyToManyField(User, related_name='likes')

class Answer(models.Model):
    text     = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    raiting  = models.IntegerField()
    question = models.ForeignKey(Question)
    author   = models.ManyToManyField(User)


