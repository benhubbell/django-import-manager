import bcrypt
import os
import secrets

from django.core.management.base import BaseCommand

from dotenv import load_dotenv
from django.utils import timezone
from core.models import SignUpKey


class Command(BaseCommand):
    help = 'Create invite link'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username')
        parser.add_argument('duration_in_minutes', type=int, help='Duration in minutes')

    def handle(self, *args, **kwargs):
        load_dotenv()
        username = kwargs['username']
        duration_in_minutes = kwargs['duration_in_minutes']

        token = secrets.token_urlsafe(100)

        salt = bcrypt.gensalt()
        print(salt)
        hashed_token = bcrypt.hashpw(bytes(token, 'utf-8'), salt)

        signupKey = SignUpKey.objects.create(
            username=username,
            salt=salt.decode('utf-8'),
            hashed_token=hashed_token.decode('utf-8'),
            duration_in_minutes=duration_in_minutes
        )

        return f'/auth/signup?username={username}&token={token}'