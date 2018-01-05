"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView



from django.conf import settings
from django.conf.urls.static import static
from blog import views
# from untitled.core import views as core_views

import django_rq.urls

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),

    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.home, name="home"),
    url(r'', include('blog.urls')),
    url(r'^django-rq/', include('django_rq.urls')),
    # for authentication system
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


