from django.test import SimpleTestCase
from django.urls import resolve, reverse
from members.urls import urlpatterns

class TestUrls(SimpleTestCase):
    # Testa se a URL 'kanban' está configurada corretamente
    def test_kanban_url_resolves(self):
        url = reverse('kanban')
        self.assertEqual(resolve(url).url_name, 'kanban')

    # Testa se a URL 'update_task_status' está configurada corretamente
    def test_update_task_status_url_resolves(self):
        url = reverse('update_task_status', args=[1])
        self.assertEqual(resolve(url).url_name, 'update_task_status')

    # Testa se a URL 'profile_list' está configurada corretamente
    def test_profile_list_url_resolves(self):
        url = reverse('profile_list')
        self.assertEqual(resolve(url).url_name, 'profile_list')

    # Testa se a URL 'delete_announcement' está configurada corretamente
    def test_delete_announcement_url_resolves(self):
        url = reverse('delete_announcement', args=[1])
        self.assertEqual(resolve(url).url_name, 'delete_announcement')

    # Testa se a URL 'delete_event' está configurada corretamente
    def test_delete_event_url_resolves(self):
        url = reverse('delete_event', args=[1])
        self.assertEqual(resolve(url).url_name, 'delete_event')

    # Testa se a URL 'taskBoard' está configurada corretamente
    def test_task_board_url_resolves(self):
        url = reverse('taskBoard')
        self.assertEqual(resolve(url).url_name, 'taskBoard')
