from django.test import TestCase
from guest.models import AdmissionState

class AdmissionStateModelTest(TestCase):

    def test_create_admission_state(self):
        # Testa a criação de um novo AdmissionState
        admission_state = AdmissionState.objects.create(is_open=True)
        
        # Verifica se o estado foi salvo corretamente
        self.assertEqual(admission_state.is_open, True)
        
    def test_default_admission_state(self):
        # Testa se o valor default do is_open é True
        admission_state = AdmissionState.objects.create()
        
        # Verifica se o valor default de is_open é True
        self.assertEqual(admission_state.is_open, True)
    
 
