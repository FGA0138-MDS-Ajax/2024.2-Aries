from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class LoginTests(TestCase):

    def setUp(self):
        # Cria um usuário para testar o login
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='password123'
        )

    def test_login_get(self):
        # Testa a renderização da página de login
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_post_success(self):
        # Testa o login com sucesso
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password123'})
        self.assertRedirects(response, reverse('home'))

    def test_login_post_failure(self):
        # Testa o login com falha
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  # O login falhou, então permanece na página de login
        self.assertTemplateUsed(response, 'login.html')

class RegisterTests(TestCase):

    def setUp(self):
        # Cria um superusuário para garantir que o teste tenha permissões de admin
        self.superuser = get_user_model().objects.create_superuser(
            username='admin',
            password='adminpassword',
            email='admin@example.com'
        )

    def test_register_get(self):
        # Testa a renderização da página de cadastro para superusuário
        self.client.login(username='admin', password='adminpassword')  # Faz login como superusuário
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_post_success(self):
        # Testa o envio do formulário com dados válidos
        self.client.login(username='admin', password='adminpassword')  # Faz login como superusuário
        data = {
            'fullname': 'Test User',
            'email': 'testuser@example.com',
            'username': 'newuser',
            'phone': '123456789',
            'areas': [1], 
            'functions': [1],  
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200) 

    def test_register_post_failure(self):
        # Testa o envio do formulário com dados inválidos
        self.client.login(username='admin', password='adminpassword')  # Faz login como superusuário
        data = {
            'fullname': '',  # Nome vazio
            'email': 'invalid_email',  # Email inválido
            'username': 'newuser',
            'phone': '123456789',
            'areas': [1],
            'functions': [1],
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)  # A página de erro é renderizada
        self.assertEqual(get_user_model().objects.filter(username='newuser').count(), 0)


class RecoverAccountTests(TestCase):

    def test_recover_account_post_success(self):
        # Cria um usuário para testar a recuperação de conta
        user = get_user_model().objects.create_user(
            username='testuser',
            password='password123',
            email='testuser@example.com'
        )
        
        # Envia a solicitação de recuperação de conta
        response = self.client.post(reverse('recoverAccount'), {'email': 'testuser@example.com'})
        
        # Verifica o status da resposta
        self.assertEqual(response.status_code, 200)

      
        response_json = response.json()
        self.assertIn('mensagem', response_json)
        self.assertEqual(response_json['mensagem'], 'Enviamos um email de recuperação de conta para testuser@example.com, cheque em sua caixa postal.')
    
    def test_recover_account_post_failure(self):
        response = self.client.post(reverse('recoverAccount'), {'email': 'nonexistent@example.com'})
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('mensagem', response_json)
        self.assertEqual(response_json['mensagem'], 'Este email não existe, é necessário que o email tenha registro no sistema para recuperá-lo.')

class EditUserTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='password123'
        )
        self.client.login(username='testuser', password='password123')

    def test_edit_user_get(self):
        response = self.client.get(reverse('editar_usuario'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pagConfig.html')

    def test_edit_user_post(self):
        data = {
            'fullname': 'New Name',
            'email': 'newemail@example.com',
            'username': 'newusername',
            'phone': '987654321',
        }
        response = self.client.post(reverse('editar_usuario'), data)
        self.user.refresh_from_db()
        self.assertEqual(self.user.fullname, 'New Name')
        self.assertEqual(self.user.email, 'newemail@example.com')
        self.assertRedirects(response, reverse('pagConfig'))
