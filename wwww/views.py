from django.shortcuts import render, redirect
from django.db import models
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from blog.models import blog
from song.models import song
from video.models import video
from video.views import videoEachCategory


def index(request):
    blogs = blog.objects.all()[:3]
    songs = song.objects.all()[:3]
    videos = video.objects.all()[:2]
    list_category_video = video.objects.values_list(
        'category', flat=True).distinct()[:3]

    print(list_category_video)
    context = {
        'list_blog': blogs,
        'list_song': songs,
        'list_video': videos,
        'page': 'Home',
        'list_category_blog': list_category_video,

    }
    print('list_blog')

    return render(request, 'index.html', context)


class indexListView(TemplateView, videoEachCategory):
    template_name = 'web/index.html'
    extra_context = {
        'page': 'Homepage'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        blogs = blog.objects.all()[:4]
        kwargs.update({'list_blog': blogs, })

        songs = song.objects.all()[:4]
        kwargs.update({'list_song': songs, })

        videos = video.objects.all()[:6]
        kwargs.update({'list_video': videos, })

        querysets = self.get_latest_video_each_kategori()
        kwargs.update({'latest_video_list': querysets})

        return super().get_context_data(*args, **kwargs)


def adminpage(request):
    blogs = blog.objects.all()
    songs = song.objects.all()
    videos = video.objects.all()
    context = {
        'blogs': blogs,
        'videos': videos,
        'songs': songs,
        'page': 'pageAdmin'
    }
    print(request.user.is_authenticated())

    template_name = None
    if request.user.is_authenticated():
        # logika untuk user
        # return redirect('adminpage')
        template_name = 'admin/adminpage.html'
    else:
        # logika untuk anonymous
        template_name = 'admin/login.html'
        # return redirect('adminlogin')
    # template_name = None
    # if request.user.is_authenticated():
    #     return redirect('adminpage')
    # else:
    #     return redirect('index')
    return render(request, template_name, context)


# def loginadmin(request):
#     context = {
#         '': '',
#     }
#     user = None

#     if request.method == "GET":
#         if request.user.is_authenticated():
#             return redirect('adminpage')
#         else:
#             # return redirect('login')
#             return render(request, 'admin/login.html', context)

#     if request.method == "POST":
#         username_login = request.POST['username']
#         password_login = request.POST['password']

#         user = authenticate(
#             request, username=username_login, password=password_login)

#         if user is not None:
#             login(request, user)
#             return redirect('homepageadmin')
#         else:
#             return redirect('login')

def adminlogin(request):
    context = {
        'page_title': 'LOGIN',
    }
    user = None

    if request.method == "GET":
        if request.user.is_authenticated():
            # logika untuk user
            return redirect('adminpage')
        else:
            # logika untuk anonymous
            return render(request, 'admin/login.html', context)

    if request.method == "POST":

        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login,
                            password=password_login)

        if user is not None:
            login(request, user)
            return redirect('adminpage')
        else:
            return redirect('login')


@login_required
def adminlogout(request):
    context = {
        'page': 'Logout Admin',
    }
    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)
        return redirect('index')

    return render(request, 'admin/logout.html', context)
