# создание курсов
from django.core.management import BaseCommand

from curs.models import Course


class Command(BaseCommand):

    def handle(self, *args, **options):
        # создание объектов курс
        Course.objects.bulk_create([
            Course(title='1', description='about fucking get'),
            Course(title='2', description='get ball'),
        ])
