from django.urls import path

from curs.apps import CursConfig
from rest_framework.routers import DefaultRouter

from curs.views.courses import CourseViewSet
from curs.views.lessons import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView
from curs.views.payments import PaymentsListAPIView

app_name = CursConfig.name

router = DefaultRouter()
router.register(r'curs', CourseViewSet, basename='curs')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('course/payments/', PaymentsListAPIView.as_view(), name='payments'),

] + router.urls
