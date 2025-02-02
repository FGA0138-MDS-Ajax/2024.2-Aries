from django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from report.models import FlightLog
from Users.models import MembroEquipe

class FlightLogViewTests(TestCase):
    
    def setUp(self):
        # Criar um membro da equipe para associar aos voos
        self.membro = MembroEquipe.objects.create(
            username="testuser", 
            fullname="Test Membro", 
            email="testmembro@example.com",
            phone="123456789",
            areaUsuario=MembroEquipe.AreaChoices.SOFTWARE_ENGINEERING
        )
        
        # Criar um voo para testar as views
        self.flight_log = FlightLog.objects.create(
            date="2025-02-01",
            start_time="12:00:00",
            end_time="14:00:00",
            document_username="test_user",
            pilot_name="Test Pilot",
            location="Test Location",
            team_members="Test Team",
            flight_success_rating=5,
            flight_objective_description="Test Description",
            results="Test Results",
            pilot_impressions="Test Impressions",
            improvements="Test Improvements",
            wind_speed=9.999, 
            wind_direction="North",
            atmospheric_pressure=9.999,  # Ajuste para o formato correto
            total_takeoff_weight=9.999,  
            flight_cycles=10,
            telemetry_link="http://testlink.com",
            occurred_accident=False
        )
        
        self.flight_list_url = reverse('flight_list')
        self.flight_create_url = reverse('flight_create')
        self.flight_edit_url = reverse('flight_edit', args=[self.flight_log.id])
        self.flight_delete_url = reverse('flight_delete', args=[self.flight_log.id])

    def test_flight_list_view(self):
        response = self.client.get(self.flight_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.flight_log.pilot_name)  # Verifica se o nome do piloto aparece na lista de voos

    def test_flight_create_view(self):
        response = self.client.get(self.flight_create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'report/flight_form.html')  # Verifica se o template correto é usado
        
        # Testando POST para criação de voo
        data = {
            'date': '2025-02-03',
            'start_time': '10:00:00',
            'end_time': '12:00:00',
            'document_username': 'new_user',
            'pilot_name': 'New Pilot',
            'location': 'New Location',
            'team_members': 'New Team',
            'flight_success_rating': 4,
            'flight_objective_description': 'New Description',
            'results': 'New Results',
            'pilot_impressions': 'New Impressions',
            'improvements': 'New Improvements',
            'wind_speed': 9.999,
            'wind_direction': 'South',
            'atmospheric_pressure': 9.999,
            'total_takeoff_weight': 9.999,
            'flight_cycles': 5,
            'telemetry_link': 'http://newlink.com',
            'occurred_accident': False
        }
        
        response = self.client.post(self.flight_create_url, data)
        self.assertEqual(response.status_code, 302)  # Redireciona após criação
        self.assertRedirects(response, self.flight_list_url)  # Redirecionamento para a lista de voos

    def test_flight_edit_view(self):
        response = self.client.get(self.flight_edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'report/flight_form.html')  # Verifica se o template correto é usado
        
        # Testando POST para edição de voo
        data = {
            'date': '2025-02-04',
            'start_time': '11:00:00',
            'end_time': '13:00:00',
            'document_username': 'edited_user',
            'pilot_name': 'Edited Pilot',
            'location': 'Edited Location',
            'team_members': 'Edited Team',
            'flight_success_rating': 3,
            'flight_objective_description': 'Edited Description',
            'results': 'Edited Results',
            'pilot_impressions': 'Edited Impressions',
            'improvements': 'Edited Improvements',
            'wind_speed': 9.999,
            'wind_direction': 'East',
            'atmospheric_pressure': 9.999,
            'total_takeoff_weight': 9.999,
            'flight_cycles': 15,
            'telemetry_link': 'http://editedlink.com',
            'occurred_accident': True
        }
        
        response = self.client.post(self.flight_edit_url, data)
        self.assertEqual(response.status_code, 302)  # Redireciona após edição
        self.assertRedirects(response, self.flight_list_url)  # Redirecionamento para a lista de voos
        
        # Verificar se o voo foi atualizado
        updated_flight = get_object_or_404(FlightLog, id=self.flight_log.id)
        self.assertEqual(updated_flight.pilot_name, 'Edited Pilot')

    def test_flight_delete_view(self):
        response = self.client.get(self.flight_delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'report/flight_confirm_delete.html')  # Verifica se o template correto é usado
        
        # Testando POST para exclusão de voo
        response = self.client.post(self.flight_delete_url)
        self.assertEqual(response.status_code, 302)  # Redireciona após deleção
        self.assertRedirects(response, self.flight_list_url)  # Redirecionamento para a lista de voos
        
        # Verificar se o voo foi excluído
        with self.assertRaises(FlightLog.DoesNotExist):
            FlightLog.objects.get(id=self.flight_log.id)
