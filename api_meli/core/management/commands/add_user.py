from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

UserModel = get_user_model()

class Command(BaseCommand):
    help = 'Create user demo'
    
    def handle(self, *args, **options):
        if not UserModel.objects.filter(username=os.environ.get('USERNAME', None)).exists():
            user=UserModel.objects.create_user(os.environ.get('USERNAME', None), password=os.environ.get('PASSWORD', None))
            user.is_superuser=True
            user.is_staff=True
            user.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')