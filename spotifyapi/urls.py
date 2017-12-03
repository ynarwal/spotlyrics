"""spotifyapi URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from api.urls import urlpatterns
from api import views
from django.views.static import serve
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^$', views.FrontendAppView.as_view()),
    url(r'^docs', include_docs_urls(title='Spot lyrics')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/',include(urlpatterns)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/', include('rest_auth.urls')),
]

urlpatterns += [url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': False}),]
