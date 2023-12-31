from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date').all()
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/all_blogs.html', {'page_obj': page_obj})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})

# def all_blogs(request):
#     blogs = Blog.objects.order_by('-date').all()[:5]
#     return render(request, 'blog/all_blogs.html', {'blogs': blogs})