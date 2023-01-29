from django.contrib import admin
from .models import Tag,Author,Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('date', 'author', 'title')
    list_filter = ('date', 'Tags')

    
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)

