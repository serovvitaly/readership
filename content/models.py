from django.db import models


class Source(models.Model):
    """Модель сайта - источника контента"""
    title = models.CharField(max_length=300)
    base_url = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Источник статей'
        verbose_name_plural = 'Источники статей'


class Article(models.Model):
    title = models.CharField(max_length=300)
    source_url = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    published_at = models.DateTimeField()
    content = models.TextField()
    source = models.ForeignKey(Source)

    def images(self):
        return Image.objects.filter(article_id=self.id)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Image(models.Model):
    href = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    width = models.IntegerField()
    height = models.IntegerField()
    article = models.ForeignKey(Article)

