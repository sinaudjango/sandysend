from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import video
from .forms import videoForm

# Create your views here.


class videoEachCategory():
    model = video

    def get_latest_video_each_kategori(self):
        category_list = self.model.objects.values_list(
            'category', flat=True).distinct()
        queryset = []

        for category in category_list:
            category = self.model.objects.filter(
                category=category).latest('publish')
            queryset.append(category)

        return queryset


class manageListView(ListView):
    model = video
    template_name = "admin/video/manage.html"
    context_object_name = 'video_list'

    extra_context = {
        'page': "Manage Video"
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        return super().get_context_data(*args, **kwargs)


class videoUpdateView(UpdateView):
    form_class = videoForm
    model = video
    success_url = reverse_lazy('videos:manage')
    template_name = "admin/video/update.html"


class crudView(TemplateView):
    template_name = 'video/createid.html'
    form = videoForm
    mode = None
    context = {}

    def get(self, *args, **kwargs):
        if self.mode == 'update':
            posts = video.objects.get(id=kwargs['update_id'])
            value = 'Update'
            data = posts.__dict__
            self.form = videoForm(initial=data, instance=posts)
        else:
            value = 'Tambah'
        self.context = {
            'page': 'List Video',
            'post_form': self.form,
        }
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        if kwargs.__contains__('update_id'):
            posts = video.objects.get(id=kwargs['update_id'])
            self.form = videoForm(
                self.request.POST, self.request.FiLES, instance=posts)
        else:
            self.form = videoForm(self.request.POST, self.request.FILES)
        if self.form.is_valid():
            self.form.save()
        return redirect('videos:manage')


class videoDeleteView(DeleteView):
    model = video
    template_name = "video/delete_confirmation.html"
    success_url = reverse_lazy('videos:manage')


class videoListView(ListView, videoEachCategory):
    model = video

    ordering = '-publish'
    paginate_by = 4
    template_name = "web/video/index.html"
    context_object_name = 'videolist'
    extra_context = {
        'page': 'List Video'
    }

    def get_context_data(self, *args, **kwargs):

        kwargs.update(self.extra_context)

        list_category = self.model.objects.values_list(
            'category', flat=True).distinct()
        kwargs.update({'list_category': list_category})

        list_director = self.model.objects.values_list(
            'director', flat=True).distinct()
        kwargs.update({'list_director': list_director})

        querysets = self.get_latest_video_each_kategori()
        kwargs.update({'latest_video_list': querysets})

        return super().get_context_data(*args, **kwargs)


class videoDetailView(DetailView):
    model = video
    template_name = "web/video/details.html"
    extra_context = {'page': 'Details Movies'}

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        category = self.model.objects.values_list(
            'category', flat=True).distinct()

        list_director = self.model.objects.values_list(
            'director', flat=True).distinct()
        another_movies = self.model.objects.exclude(
            slug=self.kwargs['slug'])[:4]
        related_movies = self.model.objects.filter(
            category=self.object.category).exclude(id=self.object.id)[:5]
        print(another_movies)
        self.kwargs.update({
            'list_director': list_director,
            'page': 'Details Movies',
            'another_movies': another_movies,
            'related_movies': related_movies,
            'list_category': category,
        })
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class categoryListView(ListView):
    model = video
    template_name = "web/video/index.html"
    context_object_name = 'videolist'
    ordering = '-publish'
    extra_context = {'page': 'Category Movies'}

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        list_category = self.model.objects.values_list(
            'category', flat=True).distinct()
        self.kwargs.update({'list_category': list_category})
        kwargs = self.kwargs

        list_director = self.model.objects.values_list(
            'director', flat=True).distinct()
        self.kwargs.update({'list_director': list_director})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)

    def get_queryset(self):
        self.queryset = self.model.objects.filter(
            category=self.kwargs['category'])
        print(self.queryset)
        return super().get_queryset()


class directorListView(ListView):
    model = video
    template_name = "web/video/index.html"
    context_object_name = 'videolist'

    extra_context = {'page': 'Filter by Director'}

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        list_category = self.model.objects.values_list(
            'category', flat=True).distinct()

        list_director = self.model.objects.values_list(
            'director', flat=True).distinct()
        self.kwargs.update({'list_director': list_director})
        return super().get_context_data(*args, **kwargs)

    def get_query_set(self):
        self.queryset = self.model.objects.filter(
            director=self.kwargs['director'])
        return super().get_query_set()


# class videoCreateView(CreateView):
#     form_class = videoForm
#     template_name = "video/create.html"

#     extra_context = {
#         'page': 'Add Movies',
#     }

#     def get_context_data(self, *args, **kwargs):
#         kwargs.update(self.extra_context)
#         return super().get_context_data(*args, **kwargs)

class videoCreateView(CreateView):
    form_class = videoForm
    template_name = "admin/video/create.html"


class videoCreateView2(CreateView):
    model = video
    form_class = videoForm
