from django.contrib import admin
from .models import song
# Register your models here.
class songAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug', 'time_upload',
    ]
admin.site.register(song, songAdmin)