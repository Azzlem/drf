# создание оплат

from django.core.management import BaseCommand
from curs.models import Payments, Lessons, Course
from default import cash, transfer
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        # получение объекта user
        user = User.objects.get(id=1)
        # получение объекта курс
        course = Course.objects.get(id=1)
        # получение объекта урок
        lesson = Lessons.objects.get(id=1)
        # создание объектов оплата
        Payments.objects.bulk_create([
            Payments(user=user, curs=course, amount=2000, payment_choices=cash),
            Payments(user=user, lesson=lesson, amount=3500, payment_choices=cash),
            Payments(user=user, curs=course, amount=9800, payment_choices=cash),
            Payments(user=user, lesson=lesson, amount=5000, payment_choices=transfer),
            Payments(user=user, curs=course, amount=50680, payment_choices=transfer)
        ])
