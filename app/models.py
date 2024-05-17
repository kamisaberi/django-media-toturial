from django.db import models
from  django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    profile = models.ImageField(upload_to=settings.MEDIA_ROOT)
    class Meta:
        db_table= "posts"