from django.test import TestCase
from Users.models import MembroEquipe, Area, Function
from django.db.utils import IntegrityError



class TestCase_Area_ModelTest(TestCase):
    def setUp(self):
        # Criação de um objeto Area para testar
        self.area = Area.objects.create(name="Área de Teste")

    def test_area_creation(self):
        """Testa a criação de uma instância de Area."""
        area = self.area
        self.assertEqual(area.name, "Área de Teste")
        self.assertTrue(isinstance(area, Area))
        self.assertEqual(str(area), "Área de Teste")

    def test_str_method(self):
        """Testa o método __str__ do modelo Area."""
        area = self.area
        self.assertEqual(str(area), "Área de Teste")



class MembroEquipe_Model_TestCase(TestCase):
    """Testes relacionados ao modelo MembroEquipe."""

    def setUp(self):
        """Configuração inicial para os testes, criando uma instância de MembroEquipe."""
        self.membro = MembroEquipe.objects.create_user(
            username="johndoe", 
            fullname="John Doe", 
            email="johndoe@example.com", 
            phone="1234567890", 
            password="testpassword"
        )

    def test_membro_creation(self):
        """Testa a criação de uma instância de MembroEquipe com dados válidos."""
        membro = self.membro
        self.assertEqual(membro.username, "johndoe")
        self.assertEqual(membro.fullname, "John Doe")
        self.assertEqual(membro.email, "johndoe@example.com")
        self.assertEqual(membro.phone, "1234567890")

    def test_membro_str_method(self):
        """Testa o método __str__ que deve retornar o nome de usuário."""
        membro = self.membro
        self.assertEqual(str(membro), "johndoe")

    def test_membro_creation_without_required_fields(self):
        """Testa se não é possível criar um MembroEquipe sem os campos obrigatórios."""
        with self.assertRaises(IntegrityError):
            MembroEquipe.objects.create_user(
                username="johndoe",
                fullname="",
                email="",
                phone="",
                password="testpassword"
            )