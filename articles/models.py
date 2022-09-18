import random
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.


class Article(models.Model):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)


def slugify_instance_title(instance, save=False, new_slug=None):
    if (new_slug is not None):
        slug = new_slug
    else:
        slug = slugify(instance.title)

    qs = Article.objects.filter(slug=slug).exclude(id=instance.id)
    if (qs.exists()):
        rand_int = random.randint(300_000, 500_000)
        slug = f'{slug}-{rand_int}'
        return slugify_instance_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if (save):
        instance.save()


def article_pre_save(sender, instance, **kwargs):
    if (instance.slug is None):
        slugify_instance_title(instance, save=False)

def article_post_save(sender, instance, created, **kwargs):
    if (created):
        slugify_instance_title(instance, save=True)

pre_save.connect(article_pre_save, sender=Article)


post_save.connect(article_post_save, sender=Article)