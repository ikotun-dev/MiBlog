
from django.db import models


# Create your models here.

'''The tag model '''
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

'''Model for Author that writes a pot '''
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    ''' better readable format'''
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


'''Model for a specific posts on the blog'''
class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=400)
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True, db_index=True)
    Tags = models.ManyToManyField(Tag)
    date = models.DateField(auto_now=True)
    image = models.CharField(max_length=100, null=True)


    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    

    