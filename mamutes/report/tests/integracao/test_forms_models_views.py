from django.test import TestCase, Client
from django.urls import reverse
from report.models import FlightLog
from report.forms import FlightForm
from datetime import date, time

class FlightIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.flight_data = {
            'date': date.today(),
            'start_time': time(10, 0),
            'end_time': time(11, 0),
            'document_username': "user1",
            'pilot_name': "Pilot Test",
            'location': "Test Location",
            'team_members': "Member1, Member2",
            'flight_success_rating': 5,
            'flight_objective_description': "Test Flight Objective",
            'results': "Test Results",
            'pilot_impressions': "Test Impressions",
            'improvements': "Test Improvements",
            'wind_speed': 9.999,
            'wind_direction': "North",
            'atmospheric_pressure': 9.999,
            'total_takeoff_weight': 9.999,
            'flight_cycles': 2,
            'telemetry_link': "http://example.com",
            'occurred_accident': False
        }
        self.flight = FlightLog.objects.create(**self.flight_data)
        self.list_url = reverse('flight_list')
        self.create_url = reverse('flight_create')
        self.edit_url = reverse('flight_edit', args=[self.flight.id])
        self.delete_url = reverse('flight_delete', args=[self.flight.id])

    def test_flight_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pilot Test")

    def test_flight_create_integration(self):
        form = FlightForm(data=self.flight_data)
        self.assertTrue(form.is_valid())
        response = self.client.post(self.create_url, self.flight_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(FlightLog.objects.count(), 2)

    def test_flight_edit_integration(self):
        updated_data = self.flight_data.copy()
        updated_data['pilot_name'] = "Pilot Edited"
        form = FlightForm(data=updated_data, instance=self.flight)
        self.assertTrue(form.is_valid())
        response = self.client.post(self.edit_url, updated_data)
        self.assertEqual(response.status_code, 302)
        self.flight.refresh_from_db()
        self.assertEqual(self.flight.pilot_name, "Pilot Edited")

    def test_flight_delete_integration(self):
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(FlightLog.objects.count(), 0)
