from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from .models import blog
from .forms import blogForm, ContactForm
# Create your views here.


def index(request):
    blogs = blog.objects.all()
    category = blog.objects.values_list('category', flat=True).distinct()

    paginator = Paginator(blogs, 6)
    page = request.GET.get('page')

    # Handle out of range and invalid page numbers:
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {

        'posts': blogs,
        'category_list': category
    }
    return render(request, 'web/blog/index.html', context)


def manage(request):
    blogs = blog.objects.all()
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        'posts': blogs
    }
    return render(request, 'admin/blog/manage.html', context)


class crudView(TemplateView):
    template_name = 'admin/blog/create.html'
    form = blogForm
    mode = None
    context = {}

    def get(self, *args, **kwargs):
        if self.mode == 'update':
            posts = blog.objects.get(id=kwargs['update_id'])
            value = 'Update'
            data = posts.__dict__
            self.form = blogForm(initial=data, instance=posts)
        else:
            value = 'Add'
        self.context = {
            'judul': 'Soundcloud Clone',
            'page': 'List Lagu',
            'post_form': self.form,
            'tombol': value,
        }
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        print(kwargs)
        if kwargs.__contains__('update_id'):
            posts = blog.objects.get(id=kwargs['update_id'])
            self.form = blogForm(
                self.request.POST, self.request.FILES, instance=posts)
        else:
            self.form = blogForm(self.request.POST, self.request.FILES)
        if self.form.is_valid():
            self.form.save()
        return redirect('blogs:manage')


def update(request, update_id):
    posts = blog.objects.get(id=update_id)
    data = posts.__dict__
    temp = {
        'title': posts.title,
        'content': posts.content,
        'category': posts.category,
        'author': posts.author,
        'cover': posts.cover,

    }
    post_form = blogForm(request.POST, request.FILES or None,
                         initial=temp, instance=posts)
    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()
            return redirect('blogs:manage')

    context = {
        'post_form': post_form
    }
    return render(request, 'admin/blog/create.html', context)


def delete(request, delete_id):
    blog.objects.filter(id=delete_id).delete()
    return redirect('blogs:manage')


def create(request):
    form_class = blogForm
    post_form = blogForm(request.POST, request.FILES or None)
    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()
            return redirect('blogs:manage')
    context = {
        'post_form': post_form,

    }
    return render(request, 'admin/blog/create.html', context)


class blogCreateView(CreateView):
    form_class = blogForm
    template_name = "admin/blog/create2.html"


def category(request, categoryInput):
    blogs = blog.objects.filter(category=categoryInput)
    category = blog.objects.values_list('category', flat=True).distinct()
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')

    # Handle out of range and invalid page numbers:
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {

        'posts': blogs,
        'category_list': category,
        'page': 'Blog Category'
    }
    return render(request, 'web/blog/index.html', context)

# def details(request, slugInput):
#     post = blog.objects.get(slug=slugInput)
#     context = {
#         'page':'Details Blog',
#         'posts':post,
#     }
#     return render(request, 'blog/details.html', context)


def details(request, slugInput):
    posts = blog.objects.get(slug=slugInput)
    category = blog.objects.values_list('category', flat=True).distinct()
    related = blog.objects.filter(
        category=posts.category).exclude(id=posts.id)[:5]
    print(related)
    context = {
        'page': 'Details Blog',
        'post': posts,
        'category_list': category,
        'related_posts': related,
    }
    return render(request, 'web/blog/details.html', context)
