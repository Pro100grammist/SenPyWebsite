import logging
from django.shortcuts import render
from django.utils.translation import activate
from portfolio.models import *


def home(request, language=None):
    if language:
        activate(language)
        request.LANGUAGE_CODE = language

        # Initializing the logger for debugging
        logger = logging.getLogger(__name__)
        logger.debug(request.LANGUAGE_CODE)

    data_mapping = {
        'projects': Projects.objects.all(),
        'hard_skills': HardSkill.objects.all(),
        'necessary_useful': NecessaryUseful.objects.all(),
    }

    return render(request, 'portfolio/homepage.html', context=data_mapping)


def about(request):

    certificates = Certificates.objects.all()
    return render(request, 'portfolio/about.html', {'certificates': certificates})


def sub_page(request, content_key):

    model_mapping = {
        'ide': IDE,
        'web_frameworks': WebFrameworks,
        'data': Data,
        'webserver': WebServers,
        'frontend': FrontEnd,
        'paas': PaaS,
        'git_serv': GitServices
    }

    model = model_mapping.get(content_key)
    items = [] if model is None else model.objects.all()

    return render(request, 'portfolio/sub_page.html', {'items': items})
