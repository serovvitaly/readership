from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    source_id = models.IntegerField()


class Source(models.Model):
    """Модель сайта - источника контента"""
    title = models.CharField(max_length=300)
    base_url = models.CharField(max_length=300)
    description = models.TextField()
