from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from main.models import Currency
from .serializers import CurrencySerializer


class CurrencyListView(ListAPIView):
    queryset = Currency.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CurrencySerializer


class CurrencyDetailView(RetrieveAPIView):
    queryset = Currency.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CurrencySerializer
