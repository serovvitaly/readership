from django.contrib import admin
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class GroupAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
    list_display = ('name', 'description')

admin.site.register(Group, GroupAdmin)
