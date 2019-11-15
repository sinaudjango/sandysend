from django.contrib import admin
from .models import video
# Register your models here.
class adminVideo(admin.ModelAdmin):
    readonly_fields = ['slug', 'publish', 'update',]

admin.site.register(video, adminVideo)