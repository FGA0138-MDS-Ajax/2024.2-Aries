from django.test import TestCase
from django.urls import reverse
from guest.models import AdmissionState

class ViewsTests(TestCase):

    def setUp(self):
        # Garantir que o estado de admissão seja criado com id=1
        self.admission_state, _ = AdmissionState.objects.get_or_create(id=1, defaults={'is_open': True})

    def test_index_view(self):
        # Testa se a view 'index' renderiza o template correto
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_competition_view(self):
        # Testa se a view 'competition' renderiza o template correto
        response = self.client.get(reverse('competition'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comp.html')

