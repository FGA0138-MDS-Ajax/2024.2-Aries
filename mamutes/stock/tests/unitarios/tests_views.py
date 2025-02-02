from django.test import TestCase, Client
from django.urls import reverse
from stock.models import Tool
from Users.models import MembroEquipe


class ToolViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.tool = Tool.objects.create(
            name="Furadeira",
            type="Elétrica",
            code="12345",
            brand="Bosch",
            quantity=10,
            observation="Nova",
            location="Almoxarifado",
            being_used=False
        )
        # Cria um usuário do modelo MembroEquipe e faz login
        self.user = MembroEquipe.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_stock_view(self):
        # Testa se a visualização da página de estoque retorna o status 200 e exibe o template correto
        response = self.client.get(reverse('stock'))  
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'stock.html')  
        self.assertContains(response, self.tool.name)  # Verifica se o nome da ferramenta "Furadeira" aparece na página

    def test_adicionar_ferramenta(self):
        # Testa a adição de uma nova ferramenta no sistema
        response = self.client.post(reverse('adicionar_ferramenta'), {
            'name': 'Martelo',
            'type': 'Manual',
            'code': '67890',
            'brand': 'Tramontina',
            'quantity': 5,
            'observation': 'Usado',
            'location': 'Oficina',
            'being_used': 'on'
        })
        self.assertEqual(response.status_code, 302)  # Verifica se ocorre um redirecionamento após a criação
        self.assertTrue(Tool.objects.filter(name='Martelo').exists())  # Verifica se a nova ferramenta foi salva no banco de dados

    def test_editar_ferramenta(self):
        # Testa a edição de uma ferramenta existente
        response = self.client.post(reverse('editar_ferramenta', args=[self.tool.pk]), {
            'name': 'Furadeira Alterada',
            'type': 'Elétrica',
            'code': '12345',
            'brand': 'Bosch',
            'quantity': 15,
            'observation': 'Revisada',
            'location': 'Almoxarifado',
            'being_used': 'on'
        })
        self.assertEqual(response.status_code, 302)  # Verifica se ocorre um redirecionamento após a edição
        self.tool.refresh_from_db()  # Atualiza a ferramenta para garantir que os dados estão atualizados
        self.assertEqual(self.tool.name, 'Furadeira Alterada')  # Verifica se o nome foi alterado corretamente
        self.assertEqual(self.tool.quantity, 15)  # Verifica se a quantidade foi alterada corretamente
        self.assertEqual(self.tool.observation, 'Revisada')  # Verifica se a observação foi alterada corretamente

    def test_deletar_ferramenta(self):
        # Testa a exclusão de uma ferramenta do banco de dados
        response = self.client.post(reverse('deletar_ferramenta', args=[self.tool.pk]))  
        self.assertEqual(response.status_code, 302)  # Verifica se ocorre um redirecionamento após a exclusão
        self.assertFalse(Tool.objects.filter(pk=self.tool.pk).exists())  # Verifica se a ferramenta foi removida do banco de dados

    def test_download_csv(self):
        # Testa se o arquivo CSV das ferramentas é gerado corretamente
        response = self.client.get(reverse('download_csv'))  
        self.assertEqual(response.status_code, 200)  # Verifica se a resposta foi bem-sucedida
        self.assertEqual(response['Content-Type'], 'text/csv')  # Verifica se o tipo de conteúdo é CSV
        self.assertIn('Furadeira', response.content.decode())  # Verifica se o nome da ferramenta está no conteúdo do CSV

    def test_download_pdf(self):
        # Testa se o arquivo PDF das ferramentas é gerado corretamente
        response = self.client.get(reverse('download_pdf'))  
        self.assertEqual(response.status_code, 200)  # Verifica se a resposta foi bem-sucedida
        self.assertEqual(response['Content-Type'], 'application/pdf')  # Verifica se o tipo de conteúdo é PDF
