from django.db import models


class Image(models.Model):
    """A constrict model for Image"""
    file = models.ImageField(upload_to='images/')
