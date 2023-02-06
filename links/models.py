from django.db import models

# Create your models here.

class Link(models.Model):
    social_media_name = models.CharField(max_length=255)
    social_media_link = models.CharField(max_length=300)
    social_media_image_white = models.CharField(max_length=255)
    social_media_image = models.CharField(max_length=255)
    notes = models.CharField(max_length=300)

