from django.core.management import BaseCommand, CommandError
from argparse import ArgumentParser
from core.models import User


class Command(BaseCommand):
    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-p', '--phone', help='please enter your phone number', required=True)

    def handle(self, *args, **options):
        phone = options['phone']
        try:
            user = User.objects.get(phone=phone)
            user.is_active = True
            user.save()
            # print(self.style.SUCCSESS(f'is_active {user}'))
            self.stdout.write(self.style.SUCCESS(f'is_active {user}'))
        except:
            raise CommandError('user not find')
