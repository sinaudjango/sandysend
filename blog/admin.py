from django.contrib import admin
from .models import blog
# Register your models here.
class adminBlog(admin.ModelAdmin):
    readonly_fields = ['slug', 'publish', 'update',]
admin.site.register(blog, adminBlog)
