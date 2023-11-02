"""
URL configuration for my_portfolio_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'), name='blog'),
    path('about/', views.about, name='about'),
    path('<str:content_key>/', views.sub_page, name='ide'),
    path('<str:content_key>/', views.sub_page, name='web_frameworks'),
    path('<str:content_key>/', views.sub_page, name='data'),
    path('<str:content_key>/', views.sub_page, name='webserver'),
    path('<str:content_key>/', views.sub_page, name='frontend'),
    path('<str:content_key>/', views.sub_page, name='git_serv'),
    path('<str:content_key>/', views.sub_page, name='paas'),
    path('<str:content_key>/', views.sub_page, name='education'),
    path('<str:content_key>/', views.sub_page, name='coding_simulator'),
    path('<str:language>/', views.home, name='home_with_language'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
