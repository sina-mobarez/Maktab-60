from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=400)
    created_on = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    