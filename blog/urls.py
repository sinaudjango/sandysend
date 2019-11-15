from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import index, details, category, manage, create, blogCreateView, delete, update, crudView

urlpatterns = [
    # url(r'^update/(?P<update_id>[0-9]+)/$', update, name='update'),
    url(r'^delete/(?P<delete_id>[0-9]+)/$', delete, name='delete'),
    url(r'^update/(?P<update_id>[0-9]+)/$',
        crudView.as_view(mode='update'), name='update'),
    url(r'^create/', crudView.as_view(mode='create'), name='create'),
    url(r'^create2/$', blogCreateView.as_view(), name='create2'),
    # url(r'^create/$', create, name='create'),
    url(r'^manage/$', manage, name='manage'),
    url(r'^category/(?P<categoryInput>[\w-]+)/$', category, name='category'),
    # url(r'^details/$', TemplateView.as_view(template_name='web/blog/details.html'), name='details'),
    url(r'^details/(?P<slugInput>[\w-]+)/$', details, name='details'),
    url(r'^$', index, name='index'),
]
