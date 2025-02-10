from django.test import TestCase, Client
from django.urls import reverse
from Users.models import MembroEquipe
from stock.models import Tool

class StockViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

        # Cria um usuário de teste
        self.user = MembroEquipe.objects.create_user(
            username='testuser',
            password='testpassword',
            fullname="Test User", 
            email="test@example.com",
            phone="123456789"
        )

        self.client.login(username='testuser', password='testpassword')  # Autenticação

        self.tool = Tool.objects.create(
            name="Martelo",
            type="Manual",
            code="MRT123",
            brand="Tramontina",
            quantity=10,
            observation="Uso geral",
            location="Depósito A",
            being_used=False
        )
        self.add_url = reverse('adicionar_ferramenta')
        self.edit_url = reverse('editar_ferramenta', args=[self.tool.id])
        self.delete_url = reverse('deletar_ferramenta', args=[self.tool.id])
        self.stock_url = reverse('stock')
        self.pdf_url = reverse('download_pdf')
        self.csv_url = reverse('download_csv')

    def test_adicionar_ferramenta(self):
        response = self.client.post(self.add_url, {
            'name': 'Chave de Fenda',
            'type': 'Manual',
            'code': 'CFD456',
            'brand': 'Bosch',
            'quantity': '5',
            'observation': 'Uso profissional',
            'location': 'Depósito B',
            'being_used': 'on'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tool.objects.count(), 2)

    def test_editar_ferramenta(self):
        response = self.client.post(self.edit_url, {
            'name': 'Martelo de Borracha',
            'type': 'Manual',
            'code': 'MRT123',
            'brand': 'Tramontina',
            'quantity': '8',
            'observation': 'Para superfícies delicadas',
            'location': 'Depósito C',
            'being_used': 'off'
        })
        self.assertEqual(response.status_code, 302)
        self.tool.refresh_from_db()
        self.assertEqual(self.tool.name, 'Martelo de Borracha')

    def test_deletar_ferramenta(self):
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tool.objects.count(), 0)

    def test_download_pdf(self):
        response = self.client.get(self.pdf_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')

    def test_download_csv(self):
        response = self.client.get(self.csv_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')

    def test_stock_view(self):
        response = self.client.get(self.stock_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Martelo")
