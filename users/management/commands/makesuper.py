from django.core.management.base import BaseCommand
from users.models import CusetomUser
from resume.models import Resume
from allauth.account.models import EmailAddress

class Command(BaseCommand):
    help = 'Create super user'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        qs = CusetomUser.objects.filter(username='admin')
        if not qs.exists():
            user = CusetomUser.objects.create_superuser(
                'admin',
                'jigneshkotadiya000@gmail.com',
                'admin'
            )

            # all auth email addres verify
            obj, created = EmailAddress.objects.get_or_create(user_id=user.id, verified=1, primary=1, email=user.email)
            obj.save()

            # resume table object create
            obj, created = Resume.objects.get_or_create(user_id=user.id)
            obj.is_student = True
            obj.save()

