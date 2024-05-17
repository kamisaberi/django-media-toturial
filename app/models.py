from django.db import models
from  django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    profile = models.ImageField(upload_to=settings.MEDIA_ROOT)

    def __str__(self) -> str:
        return f"title :{self.title} content:{self.content} profile:{self.profile}"
    def __repr__(self) -> str:
        return f"title :{self.title} content:{self.content} profile:{self.profile}"
    class Meta:
        db_table= "posts"