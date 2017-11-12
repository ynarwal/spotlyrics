from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Create superuser'

    def handle(self, *args, **options):
        username = 'admin'
        password = os.environ.get('ADMIN_PASSWORD')
        email = os.environ.get('ADMIN_EMAIL')
        User.objects.create_superuser(username, email, password)
        self.stdout.write(self.style.SUCCESS('Successfully created superuser "%s"' % username))