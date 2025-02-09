from django.db.utils import IntegrityError
from django.test import TestCase
import datetime
from datetime import time
from report.models import FlightLog, Minutes
from Users.models import MembroEquipe
from django.db import IntegrityError
from decimal import Decimal




class MinutesModelTest(TestCase):

    def setUp(self):
        """
        Configura os dados necessários para os testes.
        Criando um MembroEquipe para ser associado ao Minutes.
        """
        # Correção do nome do campo, de 'name' para 'fullname'
        self.member = MembroEquipe.objects.create(
            fullname="Membro Teste",  # Campo correto: 'fullname'
            email="membro@teste.com",  # Campo correto: 'email'
            phone="123456789"          # Campo correto: 'phone'
        )

        self.minutes_data = {
            'date': datetime.date(2024, 1, 1),
            'title': 'Reunião de Teste',
            'content': 'Conteúdo da reunião de teste.',
            'responsible': self.member
        }

    def test_minutes_creation(self):
        """
        Testa a criação de uma instância do modelo Minutes e verifica se os campos estão corretos.
        """
        minutes = Minutes.objects.create(**self.minutes_data)

        # Verifica se o objeto foi salvo corretamente no banco de dados
        self.assertEqual(minutes.date, self.minutes_data['date'])
        self.assertEqual(minutes.title, self.minutes_data['title'])
        self.assertEqual(minutes.content, self.minutes_data['content'])
        self.assertEqual(minutes.responsible, self.minutes_data['responsible'])

    def test_string_representation(self):
        """
        Testa se a representação em string do modelo Minutes está correta.
        """
        minutes = Minutes.objects.create(**self.minutes_data)
        self.assertEqual(str(minutes), 'Reunião de Teste')

    def test_responsible_field(self):
        """
        Testa se o campo 'responsible' está associado corretamente a um objeto MembroEquipe.
        """
        minutes = Minutes.objects.create(**self.minutes_data)
        self.assertEqual(minutes.responsible.fullname, 'Membro Teste')
        self.assertEqual(minutes.responsible.email, 'membro@teste.com')
        self.assertEqual(minutes.responsible.phone, '123456789')


class FlightLogModelTest(TestCase):

    def setUp(self):
        """
        Prepara os dados necessários para os testes.
        Criando um FlightLog com dados válidos.
        """
        self.flight_log_data = {
            'date': datetime.date(2024, 1, 1),
            'start_time': datetime.time(10, 30),
            'end_time': datetime.time(11, 30),
            'document_username': 'testuser',
            'pilot_name': 'Test Pilot',
            'wind_speed': Decimal('9.999'), 
            'wind_direction': 'North',
            'atmospheric_pressure': Decimal('9.999'),  
            'total_takeoff_weight': Decimal('9.999'),  
            'flight_cycles': 2,
            'telemetry_link': 'http://example.com',
            'flight_success_rating': 4,
        }

    def test_flight_log_creation(self):
        """
        Testa a criação de um FlightLog e verifica se os campos estão corretos.
        """
        flight_log = FlightLog.objects.create(**self.flight_log_data)

        # Verifica se os campos foram salvos corretamente
        self.assertEqual(flight_log.date, self.flight_log_data['date'])
        self.assertEqual(flight_log.start_time, self.flight_log_data['start_time'])
        self.assertEqual(flight_log.end_time, self.flight_log_data['end_time'])
        self.assertEqual(flight_log.document_username, self.flight_log_data['document_username'])
        self.assertEqual(flight_log.pilot_name, self.flight_log_data['pilot_name'])
        self.assertEqual(flight_log.wind_speed, self.flight_log_data['wind_speed'])
        self.assertEqual(flight_log.wind_direction, self.flight_log_data['wind_direction'])
        self.assertEqual(flight_log.atmospheric_pressure, self.flight_log_data['atmospheric_pressure'])
        self.assertEqual(flight_log.total_takeoff_weight, self.flight_log_data['total_takeoff_weight'])
        self.assertEqual(flight_log.flight_cycles, self.flight_log_data['flight_cycles'])
        self.assertEqual(flight_log.telemetry_link, self.flight_log_data['telemetry_link'])
        self.assertFalse(flight_log.occurred_accident)


    def test_default_occurred_accident(self):
        """
        Testa o valor padrão do campo 'occurred_accident'.
        """
        flight_log = FlightLog.objects.create(**self.flight_log_data)
        self.assertFalse(flight_log.occurred_accident)



