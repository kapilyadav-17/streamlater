from django.db import models


class Video(models.Model):
    videourl = models.TextField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']