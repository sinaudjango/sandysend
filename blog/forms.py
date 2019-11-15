from django.forms import ModelForm
from django import forms
from django_summernote.widgets import SummernoteWidget
from froala_editor.widgets import FroalaEditor
from .models import blog


class blogForm(forms.ModelForm):
    """Form definition for video."""
    content = forms.CharField(widget=FroalaEditor)

    class Meta:
        """Meta definition for videoform."""

        model = blog
        fields = ('title', 'content', 'category', 'author',
                  'cover')


class ContactForm(forms.Form):
    nama_lengkap = forms.CharField(max_length=100)
    jenis_kelamin = forms.ChoiceField(choices=[
        ('p', 'pria'),
        ('w', 'wanita'),
    ])
    email = forms.EmailField(label="Alamat email")
    alamat = forms.CharField(required=False)
    kode_pos = forms.DecimalField(required=False)
    kota = forms.CharField(required=False)
    provinsi = forms.CharField(required=False)
    agree = forms.BooleanField()
