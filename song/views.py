from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, FormView, DetailView, UpdateView
from .models import song
from .forms import songForm
# Create your views here.


class songUpdateView(UpdateView):
    form_class = songForm
    model = song
    template_name = "admin/song/update.html"
    success_url = reverse_lazy('songs:manage')


class songDeleteView(DeleteView):
    model = song
    template_name = "admin/song/delete_confirmation.html"
    success_url = reverse_lazy('songs:manage')


class manageListView(ListView):
    model = song
    template_name = "admin/song/manage.html"
    context_object_name = 'song_list'
    extra_context = {
        'page': "Manage Songs"
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        return super().get_context_data(*args, **kwargs)


class songCreateView(CreateView):
    form_class = songForm
    template_name = "admin/song/create.html"


class songListView(ListView):
    model = song
    template_name = "web/song/index.html"
    paginate_by = 6
    ordering = '-time_upload'
    context_object_name = 'songlist'
    list_genre = model.objects.values_list('genre', flat=True).distinct()

    list_singer = model.objects.values_list('singer', flat=True).distinct()

    extra_context = {
        'page': 'List Songs',
        'genre_list': list_genre,
        'list_singer': list_singer
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)


class songDetailView(DetailView):
    model = song
    template_name = "web/song/details.html"
    extra_context = {
        'page': 'Details Songs',


    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        another_songs = self.model.objects.exclude(
            slug=self.kwargs['slug'])[:4]
        kwargs.update({'others': another_songs})

        related_songs = self.model.objects.filter(
            genre=self.object.genre).exclude(id=self.object.id)[:4]
        kwargs.update({'related_songs': related_songs})

        genre = self.model.objects.values_list('genre', flat=True).distinct()
        kwargs.update({'genre_list': genre})

        return super().get_context_data(*args, **kwargs)


class genreListView(ListView):
    model = song
    template_name = "web/song/index.html"
    ordering = '-time_upload'
    context_object_name = 'songlist'

    def get_queryset(self):
        self.queryset = self.model.objects.filter(genre=self.kwargs['genre'])
        print(self.queryset)
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        list_genre = self.model.objects.values_list(
            'genre', flat=True).distinct()
        self.kwargs.update({'list_genre': list_genre})
        kwargs = self.kwargs

        list_singer = self.model.objects.values_list(
            'singer', flat=True).distinct()
        self.kwargs.update({'list_singer': list_singer})
        kwargs = self.kwargs

        genre = self.model.objects.values_list('genre', flat=True).distinct()
        kwargs.update({'genre_list': genre})

        return super().get_context_data(*args, **kwargs)
