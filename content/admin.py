from django.contrib import admin
from django import forms

import content.models as models


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'source_id', )
    list_filter = ('source', )
    empty_value_display = '-empty-'
    #actions = [receive_posts]


class PostInline(admin.StackedInline):
    model = models.Article
    fields = ('title', )


class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'base_url', 'description')
    empty_value_display = '-empty-'
    #actions = [receive_posts]
    #inlines = [PostInline, ]


admin.site.register(models.Article, PostAdmin)
admin.site.register(models.Source, SourceAdmin)
