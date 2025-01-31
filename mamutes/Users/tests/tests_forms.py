from django.contrib.auth import get_user_model
from django.test import TestCase
from Users.models import MembroEquipe, Area, Function
from Users.forms import MembroEquipeChangeForm, MembroEquipeCreationForm



class MembroEquipeCreationForm_TestCase(TestCase):

    def setUp(self):
        """Configuração inicial para os testes, criando áreas e funções."""
        # Criando algumas instâncias de Area e Function para testar o formulário
        self.area = Area.objects.create(name="Desenvolvimento")
        self.function = Function.objects.create(name="Desenvolvedor")

    def test_form_valid_data(self):
        """Testa se o formulário é válido com dados corretos."""
        data = {
            'username': 'johndoe',
            'fullname': 'John Doe',
            'email': 'johndoe@example.com',
            'phone': '1234567890',
            'password1': 'testpassword',
            'password2': 'testpassword',
    
            'functions': [self.function.id],
        }
        form = MembroEquipeCreationForm(data)
        
        # Verifica se o formulário é válido
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        """Testa se o formulário é inválido quando as senhas não coincidem."""
        data = {
            'username': 'johndoe',
            'fullname': 'John Doe',
            'email': 'johndoe@example.com',
            'phone': '1234567890',
            'password1': 'testpassword',
            'password2': 'wrongpassword',  # Senhas não coincidem
            'areas': [self.area.id],
            'functions': [self.function.id],
        }
        form = MembroEquipeCreationForm(data)
        
        # Verifica se o formulário **não é válido**
        self.assertFalse(form.is_valid())

    def test_fields_in_form(self):
        """Verifica se os campos adicionais (áreas e funções) estão presentes no formulário."""
        form = MembroEquipeCreationForm()

        # Verifica se o formulário contém os campos 'areas' e 'functions'
        self.assertIn('areas', form.fields)
        self.assertIn('functions', form.fields)


class MembroEquipeChangeForm_TestCase(TestCase):

    def setUp(self):
        # Criar instâncias de área e função para o teste
        self.area_1 = Area.objects.create(name="Área 1")
        self.area_2 = Area.objects.create(name="Área 2")
        self.function_1 = Function.objects.create(name="Função 1")
        self.function_2 = Function.objects.create(name="Função 2")
        
        # Criar o MembroEquipe
        self.membro = MembroEquipe.objects.create_user(
            username="testuser", 
            email="testuser@example.com", 
            password="testpassword"
        )

    def test_form_valid_data(self):
        """Testa se o formulário é válido com dados válidos."""
        form_data = {
            'username': 'testuser',  # Username válido
            'email': 'newemail@example.com',  # Email válido
            'phone': '123456789',  # Phone válido
            'fullname': 'Test User',  # Nome completo válido
            'areas': [self.area_1.id, self.area_2.id],  # Incluindo as áreas criadas no setup
            'functions': [self.function_1.id, self.function_2.id],  # Incluindo as funções criadas no setup
        }

        form = MembroEquipeChangeForm(instance=self.membro, data=form_data)
        self.assertTrue(form.is_valid())  # Verificar se o formulário é válido

    def test_form_invalid_data(self):
        """Testa se o formulário é inválido com dados inválidos."""
        form_data = {
            'username': '',  # Username vazio (inválido)
            'email': 'invalidemail',  # Email inválido
            'phone': '123456789',  # Phone válido
            'fullname': 'Test User',  # Nome completo válido
            'areas': [self.area_1.id],  # Área válida
            'functions': [self.function_1.id],  # Função válida
        }

        form = MembroEquipeChangeForm(instance=self.membro, data=form_data)
        self.assertFalse(form.is_valid())  # Verificar se o formulário é inválido

    def test_form_no_areas_or_functions(self):
        """Testa o formulário sem selecionar áreas ou funções."""
        form_data = {
            'username': 'testuser',  # Nome de usuário válido
            'email': 'testuser@example.com',  # Email válido
            'phone': '123456789',  # Phone válido
            'fullname': 'Test User',  # Nome completo válido
            'areas': [],  # Nenhuma área selecionada
            'functions': [],  # Nenhuma função selecionada
        }
        
        form = MembroEquipeChangeForm(instance=self.membro, data=form_data)
        self.assertTrue(form.is_valid())  # Mesmo sem áreas ou funções, o formulário deve ser válido

    def test_form_invalid_area(self):
        """Testa o formulário com uma área inválida (ID inexistente)."""
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'phone': '123456789',
            'fullname': 'Test User',
            'areas': [999],  # Área inválida (ID inexistente)
            'functions': [self.function_1.id],
        }

        form = MembroEquipeChangeForm(instance=self.membro, data=form_data)
        self.assertFalse(form.is_valid())  # O formulário deve ser inválido devido à área inválida

    def test_form_invalid_function(self):
        """Testa o formulário com uma função inválida (ID inexistente)."""
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'phone': '123456789',
            'fullname': 'Test User',
            'areas': [self.area_1.id],
            'functions': [999],  # Função inválida (ID inexistente)
        }

        form = MembroEquipeChangeForm(instance=self.membro, data=form_data)
        self.assertFalse(form.is_valid())  # O formulário deve ser inválido devido à função inválida