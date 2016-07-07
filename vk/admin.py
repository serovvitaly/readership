from django.contrib import admin
from django.db import models
from django.contrib.contenttypes.admin import GenericForeignKey


admin.site.site_title = 'Админко'
admin.site.site_header = 'Админко'


class Group(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


def receive_posts(modeladmin, request, queryset):
    #queryset.update(status='p')
    for group in queryset:
        print(group.id)
    print("Получние записей со стены")
receive_posts.short_description = "Получить записи со стены"


class Image(models.Model):
    group = models.ForeignKey(Group)


class ImageInline(GenericForeignKey):
    model = Image


class GroupAdmin(admin.ModelAdmin):
    fields = ('name', 'domain', 'description')
    list_display = ('name', 'domain', 'description')
    empty_value_display = '-empty-'
    actions = [receive_posts]


admin.site.register(Group, GroupAdmin)
