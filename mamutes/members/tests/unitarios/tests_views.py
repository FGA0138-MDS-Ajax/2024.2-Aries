from django.test import TestCase, Client
from django.urls import reverse
from members.models import MembroEquipe, Task, Event, Post, Subtask
from datetime import datetime


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = MembroEquipe.objects.create(username='testuser', fullname='Test User', email='test@example.com')
        self.task = Task.objects.create(title='Test Task', description='Task Description', status='Pendente', Prazo=datetime.now().date())
        self.event = Event.objects.create(title='Test Event', description='Event Description', member=self.user)
        self.post = Post.objects.create(title='Test Post', description='Post Description', member=self.user)

    def test_create_task_view(self):
        response = self.client.post(reverse('create_task'), {'title': 'New Task', 'description': 'Details'})
        self.assertEqual(response.status_code, 200)

    def test_delete_task_view(self):
        response = self.client.post(reverse('delete_task'), {'id_task': self.task.id})
        self.assertEqual(response.status_code, 302)

    def test_edit_task_view(self):
        response = self.client.post(reverse('edit_task'), {'id_task': self.task.id, 'title': 'Updated Task'})
        self.assertEqual(response.status_code, 302)

    def test_kanban_view(self):
        response = self.client.get(reverse('kanban'))
        self.assertEqual(response.status_code, 302)

    def test_create_post_or_event_view(self):
        response = self.client.post(reverse('create_post_or_event'), {'title': 'New Post', 'description': 'Content'})
        self.assertEqual(response.status_code, 302)

    def test_delete_announcement_view(self):
        response = self.client.post(reverse('delete_announcement', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_event_view(self):
        response = self.client.post(reverse('delete_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)

    def test_task_board_view(self):
        response = self.client.get(reverse('taskBoard'))
        self.assertEqual(response.status_code, 200)

    # def test_profile_list_view(self):
    #     response = self.client.get(reverse('profile_list'))
    #     self.assertEqual(response.status_code, 200)
