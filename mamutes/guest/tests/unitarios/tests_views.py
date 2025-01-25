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

    def test_control_admission_view(self):
        # Testa se ao enviar um POST, o estado de admissão é alterado corretamente
        state = AdmissionState.objects.get(id=1)  # Recupera o estado de admissão diretamente
        
        response = self.client.post(reverse('control_admission'))
        self.assertEqual(response.status_code, 302)  # Verifica se ocorre um redirecionamento
        
        state.refresh_from_db()  # Atualiza o estado do objeto após o POST
        self.assertFalse(state.is_open)  # Verifica se o estado foi alterado

    def test_custom_404_view(self):
        # Testa se a página 404 é renderizada corretamente
        response = self.client.get('/pagina_inexistente/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'error404.html')
