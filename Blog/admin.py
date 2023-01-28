from django.contrib import admin
from .models import Tag,Author,Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": "title"}
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)