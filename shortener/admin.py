from django.contrib import admin

from shortener import models

# Register your models here.


class UrlAdmin(admin.ModelAdmin):
    model = models.Url
    fields = [
        'url',
        'shorten_link',
        'visits_count',
        'user',
    ]
    readonly_fields = [
        'visits_count',
        'user',
    ]
    list_display = [
        'url',
        'shorten_link',
        'user',
        'visits_count',
    ]
    search_fields = [
        'user__username',
    ]


admin.site.register(models.Url, UrlAdmin)
