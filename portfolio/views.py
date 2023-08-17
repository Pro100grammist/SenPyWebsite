from django.shortcuts import render
from .models import Projects


def home(request):
    projects = Projects.objects.all()
    return render(request, 'portfolio/homepage.html', {'projects': projects})


def about(request):
    return render(request, 'portfolio/about.html')
