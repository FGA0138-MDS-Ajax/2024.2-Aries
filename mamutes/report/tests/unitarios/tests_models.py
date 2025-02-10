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
        self.member = MembroEquipe.objects.create(
            fullname="Membro Teste",
            email="membro@teste.com",
            phone="123456789"
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
        A função deve criar uma instância de Minutes com os dados fornecidos e garantir que os campos 
        correspondem corretamente aos valores passados.
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
        A função deve retornar a string do título da reunião quando a instância do modelo for chamada.
        """
        minutes = Minutes.objects.create(**self.minutes_data)
        self.assertEqual(str(minutes), 'Reunião de Teste')

    def test_responsible_field(self):
        """
        Testa se o campo 'responsible' está associado corretamente a um objeto MembroEquipe.
        A função deve garantir que os dados do responsável estejam corretos ao acessar o campo.
        """
        minutes = Minutes.objects.create(**self.minutes_data)
        self.assertEqual(minutes.responsible.fullname, 'Membro Teste')
        self.assertEqual(minutes.responsible.email, 'membro@teste.com')
        self.assertEqual(minutes.responsible.phone, '123456789')


class FlightLogModelTest(TestCase):
    
    def setUp(self):
        """
        Configura os dados necessários para os testes do modelo FlightLog.
        Cria um membro da equipe e os dados iniciais para um FlightLog.
        """
        self.team_member = MembroEquipe.objects.create(
            username="membro_teste",  # Adiciona um username único
            fullname="Membro Teste",
            email="membro@teste.com",
            phone="123456789"
        )

        self.flight_log_data = {
            'date': datetime.date(2024, 1, 1),
            'start_time': datetime.time(10, 30),
            'end_time': datetime.time(11, 30),
            'wind_speed': Decimal('9.999'),
            'wind_direction': 'North',
            'atmospheric_pressure': Decimal('9.999'),
            'total_takeoff_weight': Decimal('9.999'),
            'flight_cycles': 2,
            'telemetry_link': 'http://example.com',
            'flight_success_rating': 4,
            'occurred_accident': False, 
        }

    def test_flight_log_creation(self):
        """
        Testa a criação de uma instância do modelo FlightLog e verifica se os campos estão corretos.
        A função deve criar uma instância de FlightLog, associar o piloto e verificar se os dados estão 
        corretos no banco de dados.
        """
        flight_log = FlightLog.objects.create(**self.flight_log_data)

        # Associa o piloto
        flight_log.pilot_name.set([self.team_member])

        # Verificar se os campos estão corretos
        self.assertEqual(flight_log.date, self.flight_log_data['date'])
        self.assertEqual(flight_log.start_time, self.flight_log_data['start_time'])
        self.assertEqual(flight_log.end_time, self.flight_log_data['end_time'])
        self.assertTrue(flight_log.pilot_name.first() == self.team_member)  # Verifica se o piloto foi atribuído corretamente

    def test_default_occurred_accident(self):
        """
        Testa o valor padrão do campo 'occurred_accident' no modelo FlightLog.
        A função deve criar uma instância de FlightLog e verificar se o valor do campo 'occurred_accident' 
        é False por padrão.
        """
        flight_log = FlightLog.objects.create(**self.flight_log_data)
        
        # Associa o piloto
        flight_log.pilot_name.set([self.team_member])

        # Verifica se o valor de occurred_accident é False
        self.assertFalse(flight_log.occurred_accident)
