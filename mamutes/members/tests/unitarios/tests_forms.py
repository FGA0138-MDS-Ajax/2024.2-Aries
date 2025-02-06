from django.test import TestCase
from members.forms import SubtaskForm, PostForm, TaskForm, EventForm, MeetingForm

class TestForms(TestCase):
    # Testa se o formulário SubtaskForm é válido com dados corretos
    def test_subtask_form_valid(self):
        form = SubtaskForm(data={'description': 'Test subtask', 'done': False})
        self.assertTrue(form.is_valid())

    # Testa se o formulário PostForm é válido com dados corretos
    def test_post_form_valid(self):
        form = PostForm(data={'title': 'Test Post', 'description': 'Post content'})
        self.assertTrue(form.is_valid())

    # # Testa se o formulário TaskForm é válido com dados corretos
    # def test_task_form_valid(self):
    #     form = TaskForm(data={
    #         'title': 'Test Task',
    #         'description': 'Task details',
    #         'status': 'Pendente',
    #         'completion_date': '2024-12-31',
    #         'Prazo': '2024-12-31',
    #         'responsible': [],  # Se for ManyToMany, lista vazia se não obrigatório
    #         'vetor_subtasks': []  # Se for ManyToMany, lista vazia se não obrigatório
    #     })
    #     self.assertTrue(form.is_valid(), form.errors)  # Exibir erros do formulário se falhar

    # Testa se o formulário EventForm é válido com dados corretos
    def test_event_form_valid(self):
        form = EventForm(data={'title': 'Test Event', 'description': 'Event details'})
        self.assertTrue(form.is_valid())

    # # Testa se o formulário MeetingForm é válido com dados corretos
    # def test_meeting_form_valid(self):
    #     form = MeetingForm(data={
    #         'title': 'Test Meeting',
    #         'description': 'Meeting details',
    #         'meeting_date': '2024-12-31T10:00',  # Formato correto para DateTimeInput
    #         'areas': []  # Se obrigatório, substitua por IDs válidos
    #     })
    #     self.assertTrue(form.is_valid(), form.errors)  # Exibir erros do formulário se falhar
