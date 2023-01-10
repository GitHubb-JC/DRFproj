from django.db import models
from django.contrib.auth.models import User
from accounts.models import BlogUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # user 부분은 다 바꿔야 했어
    owner = models.ForeignKey(BlogUser, on_delete=models.CASCADE, blank=True, null=True, related_name='post')
    
    def __str__(self):
        return self.title
