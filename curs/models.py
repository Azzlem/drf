from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='название курса')
    preview = models.ImageField(upload_to='preview/', verbose_name='превью курса')
    description = models.TextField(verbose_name='описание курса')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lessons(models.Model):
    title = models.CharField(max_length=50, verbose_name='название урока')
    description = models.TextField(verbose_name='описание урока')
    preview = models.ImageField(upload_to='preview/', verbose_name='превью урока')
    url = models.URLField(verbose_name='ссылка на урок')

    def __str__(self):
        return f'{self.title}: {self.url}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
