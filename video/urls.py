from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib import admin
from .views import (
    videoListView,
    videoDetailView,
    categoryListView,
    videoCreateView,
    manageListView,
    videoDeleteView,
    videoUpdateView,
    crudView,
    videoCreateView2,
    directorListView,

)

urlpatterns = [
    url(r'^manage/updateid/(?P<update_id>[0-9]+)/$',
        crudView.as_view(), name='updateid'),
    url(r'^manage/update/(?P<pk>\d+)$', videoUpdateView.as_view(), name='update'),
    url(r'^manage/delete/(?P<pk>\d+)$', videoDeleteView.as_view(), name='delete'),
    url(r'^manage/$', manageListView.as_view(), name='manage'),
    # url(r'^create/$', videoCreateView.as_view(), name='create'),

    url(r'^create/$', videoCreateView.as_view(), name='create'),

    url(r'^director/(?P<director>[\w-]+)$',
        categoryListView.as_view(), name='director'),
    url(r'^category/(?P<category>[\w-]+)$',
        categoryListView.as_view(), name='category'),
    url(r'^details/(?P<slug>[\w-]+)/$',
        videoDetailView.as_view(), name='details'),
    url(r'^(?P<page>\d+)$', videoListView.as_view(), name='index'),
    # url(r'^adminpage/$',
    #     TemplateView.as_view(template_name='admin/index.html'), name='adminpage'),

    url(r'^$', videoListView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
]
