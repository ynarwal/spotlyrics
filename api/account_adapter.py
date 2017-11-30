# project/users/adapter.py:
from django.conf import settings
from rest_framework.authtoken.models import Token
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = "/account/{token}/"
        token = Token.objects.get(user=request.user)
        return path.format(token=token)