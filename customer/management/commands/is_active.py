from django.core.management import BaseCommand
from argparse import ArgumentParser
from core.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-p', '--phone', help='please enter your phone number')

    def handle(self, *args, **options):
        phone = options['phone']
        user = User.objects.get(phone=phone)
        user.is_active = True
        user.save()
        print(f'is_active {user}')

