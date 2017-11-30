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
