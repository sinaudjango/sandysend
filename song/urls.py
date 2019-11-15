from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import (
    songListView,
    songDetailView,
    genreListView,
    manageListView,
    songDeleteView,
    songUpdateView,
    songCreateView,
)


urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='song/song.html'),name='index'),
    url(r'^manage/update/(?P<pk>\d+)/$', songUpdateView.as_view(), name='update'),
    url(r'^manage/delete/(?P<pk>\d+)/$', songDeleteView.as_view(), name='delete'),
    url(r'^manage/$', manageListView.as_view(), name='manage'),
    url(r'^create/$', songCreateView.as_view(), name='create'),
    url(r'^genre/(?P<genre>[\w-]+)$', genreListView.as_view(), name='genre'),

    url(r'^details/(?P<slug>[\w-]+)$',
        songDetailView.as_view(), name='details'),
    url(r'^(?P<page>\d+)$', songListView.as_view(), name='index'),
    url(r'^$', songListView.as_view(), name='index'),
]
