from django.test import TestCase
from django.urls import reverse
from report.models import FlightLog
from decimal import Decimal  # Certifique-se de importar o Decimal

class FlightUrlsTest(TestCase):

    def test_flight_list_url(self):
        url = reverse('flight_list')  # Utilizando o nome da URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_flight_create_url(self):
        url = reverse('flight_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
