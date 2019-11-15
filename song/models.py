from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class song(models.Model):
    """Model definition for song."""
    title = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    time_upload = models.DateTimeField(auto_now_add=True)
    album = models.CharField(max_length=100)
    lyric = RichTextField()
    genre_list = (
        ('metal', 'Metal'),
        ('islamic', 'Islamic'),
        ('rnb', 'RnB'),
        ('campursari', 'Campursari'),
        ('hiphop', 'Hip Hop'),
        ('jazz', 'Jazz'),
        ('dangdut', 'Dangdut'),
        ('pops', 'Pop'),
        ('rocks', 'Rock'),

    )
    genre = models.CharField(max_length=100, choices=genre_list)
    cover = models.ImageField(
        upload_to='images/')
    audio = models.FileField(
        upload_to='songs/')
    slug = models.SlugField(editable=False, blank=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for song."""

        verbose_name = 'song'
        verbose_name_plural = 'Soundcloud'

    def __str__(self):
        """Unicode representation of song."""
        return "{}. {}".format(self.id, self.title)

    def save(self):
        self.slug = slugify(self.title)
        return super(song, self).save()

    def get_absolute_url(self):

        return reverse('songs:manage')
