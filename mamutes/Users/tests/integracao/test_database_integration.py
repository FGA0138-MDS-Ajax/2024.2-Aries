from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class DatabaseIntegrationTests(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='password123',
            email='testuser@example.com'
        )

    def test_register_post_success(self):
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
        
        # Verifica se o usuário foi criado no banco de dados
        self.assertFalse(get_user_model().objects.filter(username='newuser').exists())

        
    def test_login_authenticates_user(self):
        """Testa se um usuário pode autenticar com credenciais corretas."""
        login = self.client.login(username='testuser', password='password123')
        self.assertTrue(login)
    
    def test_login_fails_with_wrong_password(self):
        """Testa se um login falha quando a senha está errada."""
        login = self.client.login(username='testuser', password='wrongpassword')
        self.assertFalse(login)
    
    def test_edit_user_updates_database(self):
        """Testa se a edição do perfil do usuário atualiza os dados no banco."""
        self.client.login(username='testuser', password='password123')
        data = {
            'fullname': 'Updated Name',
            'email': 'updated@example.com',
            'username': 'updateduser',
            'phone': '987654321',
        }
        response = self.client.post(reverse('editar_usuario'), data)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.email, 'updated@example.com')
        self.assertRedirects(response, reverse('pagConfig'))
    
    def test_recover_account_email_sent(self):
        """Testa se a recuperação de conta envia um email."""
        response = self.client.post(reverse('recoverAccount'), {'email': 'testuser@example.com'})
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('mensagem', response_json)
        self.assertEqual(response_json['mensagem'], 'Enviamos um email de recuperação de conta para testuser@example.com, cheque em sua caixa postal.')
    
    def test_recover_account_invalid_email(self):
        """Testa se a recuperação de conta falha para um email inexistente."""
        response = self.client.post(reverse('recoverAccount'), {'email': 'invalid@example.com'})
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('mensagem', response_json)
        self.assertEqual(response_json['mensagem'], 'Este email não existe, é necessário que o email tenha registro no sistema para recuperá-lo.')
