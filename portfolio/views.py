import logging
from django.shortcuts import render, redirect
from django.utils.translation import activate, gettext_lazy as _
from portfolio.models import Projects
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
        'hard_skills': content['hard_skills'],
        'necessary_useful': content['necessary_useful'],
    }

    return render(request, 'portfolio/homepage.html', context=data_mp)


def about(request):
    """
    The view for the "About" page.
    """
    return render(request, 'portfolio/about.html', {'certificates': content['certificates']})


def sub_page(request, content_key):
    """
    Generic view for sub-pages.
    :param request: The Django request.
    :param content_key: Key for content data.
    """
    return render(request, 'portfolio/sub_page.html', {'items': content.get(content_key, [])})


