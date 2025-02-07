from django.test import TestCase, Client
from django.urls import reverse
from members.models import Task, Event, MembroEquipe
from members.forms import TaskForm, EventForm

class IntegrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.member = MembroEquipe.objects.create(fullname="Teste User")
        
    # Testa a criação de uma tarefa usando o formulário TaskForm
    def test_create_task(self):
        data = {"title": "Nova Tarefa", "description": "Descrição da tarefa", "status": "Pendente", "completion_date": "2025-12-31","Prazo": "2025-12-25","responsible": [self.member.id], "has_subtasks": False, "vetor_subtasks": ""}
        form = TaskForm(data)
        self.assertTrue(form.is_valid()) 
        task = form.save()
        task.responsible.set([self.member]) 
        self.assertEqual(task.title, "Nova Tarefa")  
        
    # Testa a criação de um evento usando o formulário EventForm
    def test_create_event(self):
        data = { "title": "Novo Evento", "description": "Descrição do evento", "event_date": "2025-12-31T10:00:00Z", "location": "Online", "is_online": True }
        form = EventForm(data)
        self.assertTrue(form.is_valid())  
        event = form.save(commit=False)
        event.member = self.member  
        event.save()
        self.assertEqual(event.title, "Novo Evento") 

    # Testa se a view taskBoard responde corretamente e contém a tarefa criada
    def test_task_view(self):
        task = Task.objects.create(title="Teste", description="Teste Desc", status="Pendente", Prazo="2025-12-25")
        response = self.client.get(reverse("taskBoard"))
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, "Teste")  


    # Testa se a view home responde corretamente e contém o evento criado
    def test_event_view(self):
        self.client.force_login(self.member)  
        event = Event.objects.create(title="Evento Teste", description="Evento Desc", event_date="2025-12-31T10:00:00Z", member=self.member)
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, "Evento Teste") 