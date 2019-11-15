from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse
from django import forms

# Create your models here.


class video(models.Model):
    """Model definition for video."""
    title = models.CharField(max_length=200)
    video = models.FileField(
        upload_to='videos/')
    thumbnail = models.ImageField(
        upload_to='images/')
    director = models.CharField(
        max_length=100, default='Frank Darabont', blank=True)
    writers = models.CharField(
        max_length=200, default='Stephen King', blank=True)
    category_list = (
        ('drama', 'Drama'),
        ('comedy', 'Comedy'),
        ('crime', 'Crime'),
        ('mystery', 'Mistery'),
        ('action', 'Action'),
        ('animation', 'Annimation'),
        ('advanture', 'Advanture'),
        ('horror', 'Horror'),
        ('war', 'War'),
        ('documentary', 'Documentary'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
        ('family', 'Family'),
        ('fantasy', 'Fantasy'),
        ('sci-fi', 'Sci-Fi'),
        ('biography', 'Biography'),
        ('musical', 'Musical'),
        ('western', 'Western'),
        ('game', 'Game'),
        ('adult', 'Adult'),
        ('short', 'Short'),
        ('talk-show', 'Talk-Show'),

    )
    category = models.CharField(
        max_length=100, choices=category_list)
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    storyline = RichTextField()
    slug = models.SlugField()
    # TODO: Define fields here

    class Meta:
        """Meta definition for video."""

        verbose_name = 'video'
        verbose_name_plural = 'Movies'

    def __str__(self):
        """Unicode representation of video."""
        return "{}.{} - {}".format(self.id, self.title, self.category)

    def save(self):
        self.slug = slugify(self.title)
        return super(video, self).save()

    def get_absolute_url(self):

        return reverse('videos:manage')
