# Команда создания нескольких уроков

from django.core.management import BaseCommand

from curs.models import Lessons, Course


class Command(BaseCommand):

    def handle(self, *args, **options):
        # получение объекта курса для последующего создания объектов Урока
        course = Course.objects.get(id=1)
        # создание уроков
        Lessons.objects.bulk_create([
            Lessons(course=course, title='second', description='about fucking get'),
            Lessons(course=course, title='third', description='about fucking get ball'),
        ])
