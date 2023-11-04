from django.core.management import BaseCommand

from curs.models import Course


class Command(BaseCommand):

    def handle(self, *args, **options):
        for el in Course.objects.all():
            print(el.lessons)
