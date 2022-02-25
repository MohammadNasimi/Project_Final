from django.core.management import BaseCommand, CommandError
from argparse import ArgumentParser
from core.models import User


class Command(BaseCommand):
    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-p', '--phone', help='please enter your phone number')

    def handle(self, *args, **options):
        phone = options['phone']
        try:
            user = User.objects.get(phone=phone)
            user.is_active = True
            user.save()
            print(self.style.SUCCESS(f'de_active {user}'))
        except:
            raise CommandError('user not find')
