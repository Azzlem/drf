

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from curs.models import Payments
from curs.serializers.payments import PaymentSerializer


class PaymentsListAPIView(generics.ListAPIView):
    # объявление серриализатора
    serializer_class = PaymentSerializer
    # объявление кверисета
    queryset = Payments.objects.all()
    # объявление фильтра
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # объявление полей фильтрации
    filterset_fields = ['curs', 'lesson', 'payment_choices']
    ordering_fields = ['date_pay']
