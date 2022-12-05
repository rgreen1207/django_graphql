from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    likes = models.IntegerField()
    reason = models.TextField()
    
    def __str__(self):
        return self.title 