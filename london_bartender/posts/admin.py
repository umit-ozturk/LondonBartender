from django.contrib import admin

from london_bartender.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "created_at", "updated_at"]
    search_fields = ["author"]
