from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from djrichtextfield.models import RichTextField
from tinymce.models import HTMLField
from tinymce import models as tinymce_models
# Create your models here.


class blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=100)
    list_author = (
        ('sandy', 'Rahmad Sandy Kurnia'),
        ('lila', 'Lailatul Murtafiah'),
        ('neima', 'Annisa Neima Kurnia'),
    )
    author = models.CharField(
        choices=list_author, max_length=100, default='neima')
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    cover = models.ImageField(
        upload_to='images/', default='images/cover.jpeg', blank=True)
    slug = models.SlugField()
    """Model definition for blog."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for blog."""

        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

    def __str__(self):
        """Unicode representation of blog."""
        return "{}.{} - {}".format(self.id, self.title, self.category)

    def save(self):
        self.slug = slugify(self.title)
        return super(blog, self).save()

    def get_absolute_url(self):
        return reverse('blogs:manage')
