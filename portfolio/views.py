import logging
from django.shortcuts import render, redirect
from django.utils.translation import activate, gettext_lazy as _
from portfolio.models import Projects


def home(request, language=None):
    if language:
        activate(language)
        request.LANGUAGE_CODE = language
        logger = logging.getLogger(__name__)  # Отримати інстанцію логгера
        logger.debug(request.LANGUAGE_CODE)  # Записати повідомлення у лог-файл
    projects = Projects.objects.all()

    return render(request, 'portfolio/homepage.html', {'projects': projects})


def about(request):
    return render(request, 'portfolio/about.html')
