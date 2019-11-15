
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView
from .views import index, indexListView, adminpage, adminlogin, adminlogout


urlpatterns = [
    url(r'^froala_editor/', include('froala_editor.urls')),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^summernote/', include('django_summernote.urls')),
    # url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^djrichtextfield/', include('djrichtextfield.urls')),

    url(r'^videdetails/$', TemplateView.as_view(template_name='videodetails.html'),
        name='videodetails'),
    url(r'^blogdetails/$',
        TemplateView.as_view(template_name='blogdetails.html'), name='blogdetails'),
    # url(r'^songs/$', TemplateView.as_view(template_name='songslist.html'),name='songs'),
    url(r'^songs/', include('song.urls', namespace='songs')),
    # url(r'^videos/$', TemplateView.as_view(template_name='videoslist.html'),name='videos'),
    url(r'^videos/', include('video.urls', namespace='videos')),
    # url(r'^blogs/$', TemplateView.as_view(template_name='blogslist.html'),name='blogs'),
    url(r'^blogs/', include('blog.urls', namespace='blogs')),
    url(r'^details/$', TemplateView.as_view(template_name='details.html'), name='details'),

    url(r'^logout/$', adminlogout, name='adminlogout'),
    url(r'^login/$', adminlogin, name='adminlogin'),
    url(r'adminpage/$', adminpage, name='adminpage'),
    # url(r'^$',
    #     TemplateView.as_view(template_name='web/index.html'), name='index'),
    url(r'^$', indexListView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
