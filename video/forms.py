from django.forms import ModelForm

from .models import video


class videoForm(ModelForm):
    """Form definition for video."""

    class Meta:
        """Meta definition for videoform."""

        model = video
        fields = ('title', 'director', 'writers', 'category',
                  'storyline', 'video', 'thumbnail', )

        # fields = [
        #     'title',
        #     'director',
        #     'writers',
        # ]
