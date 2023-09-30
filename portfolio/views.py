import logging
from django.shortcuts import render, redirect
from django.utils.translation import activate, gettext_lazy as _
from portfolio.models import Projects
from .content import skills, certificates


def home(request, language=None):
    if language:
        activate(language)
        request.LANGUAGE_CODE = language
        logger = logging.getLogger(__name__)
        logger.debug(request.LANGUAGE_CODE)

    data = {
        'projects': Projects.objects.all(),
        'hard_skills': skills['hard_skills'],
        'soft_skills': skills['soft_skills']
    }

    return render(request, 'portfolio/homepage.html', context=data)


def about(request):
    return render(request, 'portfolio/about.html', {'certificates': certificates})
