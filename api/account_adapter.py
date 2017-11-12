# project/users/adapter.py:
from django.conf import settings
from rest_framework.authtoken.models import Token
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = "{BASEPATH}/account/{token}/"
        token = Token.objects.get(user=request.user)
        return path.format(BASEPATH=settings.LOGIN_REDIRECT_URL, token=token)