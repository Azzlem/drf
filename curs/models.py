from django.contrib.auth import get_user_model
from django.db import models

from default import NULLABLE, cash, payment_choice


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='название курса')
    preview = models.ImageField(upload_to='preview/', verbose_name='превью курса', **NULLABLE)
    description = models.TextField(verbose_name='описание курса')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lessons(models.Model):
    title = models.CharField(max_length=50, verbose_name='название урока')
    description = models.TextField(verbose_name='описание урока')
    preview = models.ImageField(upload_to='preview/', verbose_name='превью урока', **NULLABLE)
    url = models.URLField(verbose_name='ссылка на урок', **NULLABLE)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='lessons')

    def __str__(self):
        return f'{self.title}: {self.url}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payments(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='пользователь', related_name='payments')
    date_pay = models.DateField(verbose_name='дата оплаты', **NULLABLE)

    curs = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, **NULLABLE)

    amount = models.IntegerField(verbose_name='сумма оплаты')
    payment_choices = models.CharField(max_length=15, choices=payment_choice, default=cash)

    def __str__(self):
        return f'{self.user} {self.curs} {self.lesson}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
