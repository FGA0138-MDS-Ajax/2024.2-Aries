from django.test import TestCase
from members.models import Task, Event, Post, Subtask, MembroEquipe, Column
from django.utils import timezone

class TestModels(TestCase):
    # Configuração inicial dos testes, criando instâncias de cada modelo
    def setUp(self):
        self.member = MembroEquipe.objects.create(fullname='Test Member')
        self.task = Task.objects.create(title='Test Task', description='Task Description', status='Pendente')
        self.event = Event.objects.create(title='Test Event', description='Event Description', member=self.member)
        self.post = Post.objects.create(title='Test Post', description='Post Description', member=self.member)
        self.subtask = Subtask.objects.create(task=self.task, description='Test Subtask', done=False)
        self.column = Column.objects.create(name='Test Column')

    # Testa a criação de uma tarefa e verifica se os atributos foram definidos corretamente
    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.status, 'Pendente')
    
    # Testa a criação de um evento e verifica se ele está associado ao membro correto
    def test_event_creation(self):
        self.assertEqual(self.event.title, 'Test Event')
        self.assertEqual(self.event.member.fullname, 'Test Member')
    
    # Testa a criação de um post e verifica se está associado ao membro correto
    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.member.fullname, 'Test Member')
    
    # Testa a criação de uma subtarefa e verifica se os atributos estão corretos
    def test_subtask_creation(self):
        self.assertEqual(self.subtask.description, 'Test Subtask')
        self.assertFalse(self.subtask.done)
    
    # Testa a criação de uma coluna e verifica se o nome foi atribuído corretamente
    def test_column_creation(self):
        self.assertEqual(self.column.name, 'Test Column')