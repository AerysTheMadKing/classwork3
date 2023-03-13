from django.db import models
from django.db import models


class Post(models.Model):
    jour_name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    place_of_events = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images')
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.title} {self.place_of_events}'



class Comment(models.Model):
    username = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f'{self.username}, {self.body}'