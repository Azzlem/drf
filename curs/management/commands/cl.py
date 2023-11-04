from django.core.management import BaseCommand

from curs.models import Lessons, Course


class Command(BaseCommand):

    def handle(self, *args, **options):
        course = Course.objects.get(id=1)

        Lessons.objects.bulk_create([
            Lessons(course=course, title='second', description='about fucking get'),
            Lessons(course=course, title='third', description='about fucking get ball'),
        ])
