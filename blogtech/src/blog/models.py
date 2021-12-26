from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.shortcuts import reverse


User = get_user_model()


class CategoryPost(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Catégorie"

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")
    image = models.ImageField(upload_to='blog')
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    category = models.ManyToManyField(CategoryPost)
    content = models.TextField(default='')
    created_on = models.DateField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Article"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    @property
    def author_unknow(self):
        if self.author:
            return self.author
        else:
            return "Auteur inconnu"

    def get_absolute_url(self):
        return reverse("posts:post-detail", kwargs={'slug': self.slug })


