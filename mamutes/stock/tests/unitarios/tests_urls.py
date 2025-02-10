from django.test import TestCase
from django.urls import reverse
from stock.models import Tool
from Users.models import MembroEquipe
from django.test import Client
from django.contrib.auth import get_user_model

class ToolUrlsTestCase(TestCase):
    def setUp(self):
        # Crie e autentique um usuário
        User = get_user_model()  
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # login
        self.client.login(username='testuser', password='testpassword')

        # Cria uma ferramenta para ser editada
        self.ferramenta = Tool.objects.create(
            name='Ferramenta Teste',
            type='Tipo Teste',
            code='1234',
            brand='Marca Teste',
            quantity=10,
            observation='Observação Teste',
            location='Local Teste',
            being_used=False
        )
    
    def test_stock_url(self):
        """Testa se a URL de estoque carrega corretamente"""
        url = reverse('stock')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_editar_ferramenta_url(self):
        """Testa se a URL de editar ferramenta redireciona corretamente"""
        url = reverse('editar_ferramenta', args=[self.ferramenta.pk])
        response = self.client.post(url, {
            'name': 'Ferramenta Teste Atualizada',
            'type': 'Tipo Atualizado',
            'code': '5678',
            'brand': 'Marca Atualizada',
            'quantity': 15,
            'observation': 'Observação Atualizada',
            'location': 'Local Atualizado',
            'being_used': 'on'
        })
        
        # Verifique se houve um redirecionamento após a edição
        self.assertEqual(response.status_code, 302)
        
        # Verifique se o redirecionamento é para a página de estoque
        self.assertRedirects(response, reverse('stock'))

    def test_deletar_ferramenta_url(self):
        """Testa se a URL de deletar ferramenta redireciona corretamente"""
        url = reverse('deletar_ferramenta', args=[self.ferramenta.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Redirecionamento após confirmação de exclusão

    def test_download_pdf_url(self):
        """Testa se a URL para download do PDF carrega corretamente"""
        url = reverse('download_pdf')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_download_csv_url(self):
        """Testa se a URL para download do CSV carrega corretamente"""
        url = reverse('download_csv')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
