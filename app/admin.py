from django.contrib import admin
from django.urls import reverse
from app import models
from django.utils.html import format_html
from django.utils.text import Truncator

per_page = 20
characters = 50

@admin.display(description='Activity', ordering='link__activity')
def get_activity(obj):
    truncator = Truncator(obj.activity.name)
    link = reverse("admin:app_activity_change", args=[obj.activity.id])
    return format_html('<a href="{}">{}</a>', link, truncator.chars(characters))

class ActivityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "user", "created_at"]
    search_fields = ['name']
    list_filter = ['hubs','user']
    list_per_page = per_page 
    

class CommentAdmin(admin.ModelAdmin):
    list_display = ['get_body', get_activity, "user", "created_at"]
    list_filter = ['user']
    list_per_page = per_page 

    @admin.display(description='Comment')
    def get_body(self, obj):
        truncator = Truncator(obj.body)
        return truncator.chars(characters)

class ProfileAdmin(admin.ModelAdmin):
    pass

class ImageAdmin(admin.ModelAdmin):
    list_display = ["file", get_activity, "user", "created_at"]
    list_filter = ['user']
    list_per_page = per_page 

class SocialAdmin(admin.ModelAdmin):
    pass

class HubAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "location", "birthday"]

class LinkAdmin(admin.ModelAdmin):
    list_display = ["get_link", get_activity, "user", "created_at"]
    search_fields = ['url']
    list_filter = ['user']
    list_per_page = per_page 

    @admin.display(description='URL')
    def get_link(self, obj):
        truncator = Truncator(obj.url)
        return truncator.chars(characters)

admin.site.register(models.Activity, ActivityAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.Social, SocialAdmin)
admin.site.register(models.Link, LinkAdmin)
admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Hub, HubAdmin)