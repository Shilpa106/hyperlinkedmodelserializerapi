from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=255) #, validators=[validate_even]
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name="posts_author",
                               on_delete=models.CASCADE,
                               null=True, blank=True)
    viewers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="posts_viewers", null=True, blank=True)

