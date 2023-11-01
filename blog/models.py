from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    cat = models.ForeignKey('PostCategory', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title
