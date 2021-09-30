from django.contrib import admin

from london_bartender.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "created_at"]
    search_fields = ["author"]
