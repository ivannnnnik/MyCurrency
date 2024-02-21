from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from main.models import Currency

EXPECTED_PAGE_SIZE = 10


class CurrencyAPITest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='test', password='test')
        cls.access_token = str(RefreshToken.for_user(cls.user).access_token)
        cls.currency = Currency.objects.create(name='USD', rate=1.0)
        Currency.objects.bulk_create([Currency(name=f'Currency {i}', rate=i) for i in range(15)])

    def setUp(self):
        self.client = APIClient()

    def test_currency_list_view_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(reverse('api:currency_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_currency_list_view_unauth(self):
        response = self.client.get(reverse('api:currency_list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_currency_detail_view(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        response = self.client.get(reverse('api:currency_detail', kwargs={'pk': self.currency.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.currency.name)
        self.assertEqual(response.data['rate'], self.currency.rate)

    def test_currency_detail_view_unauth(self):
        response = self.client.get(reverse('api:currency_detail', kwargs={'pk': self.currency.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_currency_list_view_pagination(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(reverse('api:currency_list'), {'page': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), EXPECTED_PAGE_SIZE)

        response = self.client.get(reverse('api:currency_list'), {'page': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), Currency.objects.count() - EXPECTED_PAGE_SIZE)
