from django.test import TestCase
from members.forms import SubtaskForm, PostForm, TaskForm, EventForm
from members.models import MembroEquipe, Area 
from datetime import datetime


class TestForms(TestCase):

    def setUp(self):
        # Criar o membro para ser usado nos testes
        self.member = MembroEquipe.objects.create(fullname='Test Member')
        self.area_1 = Area.objects.create(name='Test Area')

    # Testa se o formulário SubtaskForm é válido com dados corretos
    def test_subtask_form_valid(self):
        form = SubtaskForm(data={'description': 'Test subtask', 'done': False})
        self.assertTrue(form.is_valid())

    # Testa se o formulário PostForm é válido com dados corretos
    def test_post_form_valid(self):
        form = PostForm(data={'title': 'Test Post', 'description': 'Post content'})
        self.assertTrue(form.is_valid())

    # Testa se o formulário TaskForm é válido com dados corretos
    def test_task_form_valid(self):
        form_data = {
            'title': 'Test Task',
            'description': 'Task Description',
            'status': 'Pendente',
            'completion_date': datetime.now().date(),
            'Prazo': datetime.now().date(),
            'responsible': [self.member.id], 
            'has_subtasks': False, 
            'vetor_subtasks': [], 
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    # Testa se o formulário EventForm é válido com dados corretos
    def test_event_form_valid(self):
        form = EventForm(data={'title': 'Test Event', 'description': 'Event details'})
        self.assertTrue(form.is_valid())
