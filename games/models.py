from django.db import models
from django.contrib.auth import get_user_model


class Game(models.Model):
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    anything = models.CharField(max_length=256)

    def __str__(self):
        return self.anything
