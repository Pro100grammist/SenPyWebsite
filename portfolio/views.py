import logging
from django.shortcuts import render, redirect
from django.utils.translation import activate, gettext_lazy as _
from portfolio.models import *
from .content import content


def home(request, language=None):
    """
    The main view for the home page.
    :param request: The Django request.
    :param language: The selected language code.
    """
    if language:
        activate(language)
        request.LANGUAGE_CODE = language

        # Initializing the logger for debugging
        logger = logging.getLogger(__name__)
        logger.debug(request.LANGUAGE_CODE)

    data_mp = {
        'projects': Projects.objects.all(),
        'hard_skills': HardSkill.objects.all(),
        'necessary_useful': NecessaryUseful.objects.all(),
    }

    return render(request, 'portfolio/homepage.html', context=data_mp)


def about(request):
    """
    The view for the "About" page.
    """
    certificates = Certificates.objects.all()
    return render(request, 'portfolio/about.html', {'certificates': certificates})


def sub_page(request, content_key):
    """
    Generic view for sub-pages.
    :param request: The Django request.
    :param content_key: Key for content data.
    """
    model_mapping = {
        'ide': IDE,
        'web_frameworks': WebFrameworks,
        'data': Data,
    }

    model = model_mapping.get(content_key)

    if model is None:
        items = []
    else:
        items = model.objects.all()

    return render(request, 'portfolio/sub_page.html', {'items': items})
