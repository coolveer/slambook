from django.db import models
from django.contrib.auth.models import User

class Fdetail(models.Model):
    pic=models.ImageField(default='1.jpg',blank=True)
    name = models.CharField(max_length=9999)
    home = models.CharField(max_length=9999)
    pno = models.CharField(max_length=9999)
    born = models.CharField(max_length=9999)
    become = models.CharField(max_length=9999)
    dream = models.CharField(max_length=9999)
    sport = models.CharField(max_length=9999)
    relation = models.CharField(max_length=9999)
    look = models.CharField(max_length=9999)
    eat = models.CharField(max_length=9999)
    movies = models.CharField(max_length=9999)
    dislike = models.CharField(max_length=9999)
    crazy = models.CharField(max_length=9999)
    moment = models.CharField(max_length=9999)
    holiday = models.CharField(max_length=9999)
    friendship = models.CharField(max_length=9999)
    withyou = models.CharField(max_length=9999)
    hobbies = models.CharField(max_length=9999)
    truth = models.CharField(max_length=9999)
    you = models.CharField(max_length=9999)
    love = models.CharField(max_length=9999)
    date = models.CharField(max_length=9999)
    fkey = models.CharField(max_length=9999)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-pk']
    