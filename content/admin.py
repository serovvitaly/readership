from django.contrib import admin
import content.models as models


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'source_id', )
    empty_value_display = '-empty-'
    #actions = [receive_posts]


class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'base_url', 'description')
    empty_value_display = '-empty-'
    #actions = [receive_posts]


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Source, SourceAdmin)
