from django.db import models


class Challenges(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    
