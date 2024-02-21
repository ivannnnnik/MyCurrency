import xml.etree.ElementTree as ET
from typing import Any

import requests
from django.core.management.base import BaseCommand, CommandError

from main.models import Currency
from .constants import CURRENCY_URL


class Command(BaseCommand):

    def get_currencies(self):
        response = requests.get(CURRENCY_URL)
        if response.status_code != 200:
            raise CommandError(f'Request error: {response.status_code}')
        return ET.fromstring(response.content)

    def handle(self, *args: Any, **options: Any):
        try:
            # Get new currencies
            currencies = self.get_currencies()
            # Delete old currencies
            Currency.objects.all().delete()
            items = currencies.findall('.//Valute')
            currency_objects = [
                Currency(
                    name=item.find('Name').text,
                    rate=float(item.find('VunitRate').text.replace(',', '.'))
                ) for item in items
            ]
            # Create new currencies
            Currency.objects.bulk_create(currency_objects)
            self.stdout.write(self.style.SUCCESS('The currency data has been successfully added to the database.'))
        except Exception as e:
            raise CommandError(f'Error: {e}')
