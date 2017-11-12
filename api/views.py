from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import os, base64, requests, datetime
from django.contrib.auth.models import User 
from rest_framework.authtoken.models import Token
from api.services import SpotifyService

class CurrentLyricsView(APIView):

    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    service = SpotifyService()

    def get(self, request):
        data =  self.service.get_current_song_lyrics(request.user)
        return Response(status=200, data=data)

class ProfileView(APIView):

    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        print(request.user)
        return Response(status=200)


import logging
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    run build`).
    """

    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead, or
                run `yarn run build` to test the production version.
                """,
                status=501,
            )