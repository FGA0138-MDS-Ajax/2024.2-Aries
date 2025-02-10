from django.test import TestCase
from django.urls import reverse

class FlightUrlsTest(TestCase):
    def test_meetingsquadro_url(self):
        url = reverse('meetingsquadro')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Página de reuniões deve carregar

    def test_flight_list_url(self):
        url = reverse('flight_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Página de lista de voos deve carregar

    def test_flight_create_url(self):
        url = reverse('flight_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Esperando redirecionamento 

    def test_flight_edit_url(self):
        url = reverse('flight_edit', args=[1])  # Simulando edição de voo com ID 1
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Esperando redirecionamento

    def test_flight_delete_url(self):
        url = reverse('flight_delete', args=[1])  # Simulando exclusão de voo com ID 1
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Esperando redirecionamento

    def test_meetings_edit_url(self):
        url = reverse('meetings_edit', args=[1])  # Simulando edição de reunião com ID 1
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  

    def test_membros_por_area_url(self):
        url = reverse('membros_por_area', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_delete_meeting_url(self):
        url = reverse('delete_meeting', args=[1])  # Simulando exclusão de reunião ID 1
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Esperando redirecionamento
