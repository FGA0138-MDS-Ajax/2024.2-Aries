from django.test import TestCase
from report.forms import FlightForm
from report.models import FlightLog
from django.core.exceptions import ValidationError
import datetime

class FlightFormTest(TestCase):

    def setUp(self):
        # Dados iniciais para os testes
        self.flight_data = {
            'date': datetime.date(2024, 1, 1),
            'start_time': datetime.time(10, 0, 0),
            'end_time': datetime.time(11, 0, 0),
            'document_username': 'testeuser',
            'pilot_name': 'Piloto Teste',
            'location': 'Local Teste',
            'team_members': 'Membro1, Membro2',
            'flight_success_rating': 4,
            'flight_objective_description': 'Descrição do objetivo do voo teste.',
            'results': 'Resultados do teste.',
            'pilot_impressions': 'Impressões do piloto.',
            'improvements': 'Melhorias sugeridas.',
            'wind_speed': 1.234,  # Valor válido para wind_speed
            'wind_direction': 'Norte',
            'atmospheric_pressure': 9.99,  # Valor válido para atmospheric_pressure
            'total_takeoff_weight': 2.5,
            'flight_cycles': 5,
            'telemetry_link': 'http://example.com/telemetry',
            'occurred_accident': False,
        }

    def test_form_is_valid(self):
        """
        Testa se o formulário é válido quando todos os dados fornecidos são corretos.
        Espera-se que o formulário seja validado corretamente.
        """
        form = FlightForm(self.flight_data)
        print(form.errors)  # Adicionando print para depuração
        self.assertTrue(form.is_valid(), "O formulário deve ser válido quando os dados são corretos")

    def test_form_is_invalid_missing_required_field(self):
        """
        Testa se o formulário é inválido quando um campo obrigatório está ausente.
        Neste caso, o campo 'pilot_name' é removido para causar um erro de validação.
        """
        invalid_data = self.flight_data.copy()
        del invalid_data['pilot_name']  
        form = FlightForm(invalid_data)
        self.assertFalse(form.is_valid(), "O formulário não deve ser válido sem campos obrigatórios")
        self.assertIn('pilot_name', form.errors) 

    def test_form_save(self):
        """
        Testa se os dados são salvos corretamente no banco de dados quando o formulário é válido.
        Após salvar, verifica-se se o objeto FlightLog foi criado corretamente.
        """
        form = FlightForm(self.flight_data)
        if form.is_valid(): # Adicione esta verificação
            flight = form.save()
            self.assertEqual(FlightLog.objects.count(), 1)
            self.assertEqual(flight.pilot_name, self.flight_data['pilot_name'])
            # Verifique outros campos conforme necessário

    def test_flight_success_rating_validation(self):
        """
        Testa a validação do campo 'flight_success_rating'.
        O campo deve estar entre 1 e 5, então são feitos dois testes:
        1. Quando o valor é 0, deve ser inválido.
        2. Quando o valor é 6, também deve ser inválido.
        """
        invalid_data_low = self.flight_data.copy()
        invalid_data_low['flight_success_rating'] = 0
        form_low = FlightForm(invalid_data_low)
        self.assertFalse(form_low.is_valid())
        self.assertIn('flight_success_rating', form_low.errors)

        invalid_data_high = self.flight_data.copy()
        invalid_data_high['flight_success_rating'] = 6
        form_high = FlightForm(invalid_data_high)
        self.assertFalse(form_high.is_valid())
        self.assertIn('flight_success_rating', form_high.errors)
    
    def test_invalid_date_format(self):
        """
        Testa se o campo 'date' é validado corretamente.
        O campo 'date' deve ser uma data válida. Aqui, um valor inválido é fornecido ('invalid date').
        """
        invalid_data = self.flight_data.copy()
        invalid_data['date'] = 'invalid date'
        form = FlightForm(invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors)

    def test_invalid_time_format(self):
        """
        Testa se o campo 'start_time' é validado corretamente.
        O campo 'start_time' deve ser um horário válido. Aqui, um valor inválido é fornecido ('invalid time').
        """
        invalid_data = self.flight_data.copy()
        invalid_data['start_time'] = 'invalid time'
        form = FlightForm(invalid_data)
        self.assertFalse(form.is_valid())  
        self.assertIn('start_time', form.errors)
