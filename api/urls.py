from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get-current-song-lyrics/$', views.CurrentLyricsView.as_view(), name='current-lyrics'),
]