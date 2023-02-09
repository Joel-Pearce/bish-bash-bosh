from django.db import models


class Challenges(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    next_id = models.IntegerField(default=0)

    def __str__(self):
        return self.title
        
    
