from django.forms import ModelForm
from .models import song


class songForm(ModelForm):
    """Form definition for song."""

    class Meta:
        """Meta definition for songform."""

        model = song
        fields = ('title', 'singer', 'album',
                  'lyric', 'genre', 'cover', 'audio',)
