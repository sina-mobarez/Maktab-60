import random

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse

from .signals import save_comment


# Create your models here.

class Category(models.Model):
    name = models.CharField("name of category", max_length=50)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("post-category", kwargs={"pk": self.pk})


class Tag(models.Model):
    name = models.CharField("name of tag start with #", max_length=50)

    def __str__(self):
        return f'{self.name}'


# define a function to add some digit to end of slug >>>> for uniqueness
def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + str(random.randint(0, 12000))
    return unique_slug


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    slug = models.SlugField()
    bodytext = models.TextField(verbose_name="message")
    category = models.ManyToManyField(Category, verbose_name='category of this post')
    tag = models.ManyToManyField(Tag, verbose_name="tags of this post", blank=True, null=True)

    post_date = models.DateTimeField(
        auto_now_add=True, verbose_name="post date")
    modified = models.DateTimeField(null=True, verbose_name="modified", blank=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                  verbose_name="posted by",
                                  on_delete=models.SET_NULL)

    allow_comments = models.BooleanField(
        default=True, verbose_name="allow comments")
    comment_count = models.IntegerField(
        blank=True, default=0, verbose_name='comment count')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-post_date']

    # override the save method for store unique slug
    def save(self, *args, **kwargs):
        self.slug = unique_slugify(self, self.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # a method that give us slug for linking detail of post instance
    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
        }

        return reverse('post_detail', kwargs=kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                             verbose_name="name's user",
                             on_delete=models.SET_NULL)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

    # Hear a signal to save count of comment


post_save.connect(save_comment, sender=Comment)
