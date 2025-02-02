from django.test import TestCase, Client
from django.urls import reverse
from guest.models import AdmissionState

class AdmissionIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admission = AdmissionState.objects.create(is_open=True, link_admission="http://example.com")
        self.admission_url = reverse('admission')

    def test_admission_view_creates_state_if_none_exists(self):
        AdmissionState.objects.all().delete()
        response = self.client.get(self.admission_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(AdmissionState.objects.count(), 1)
        self.assertTrue(AdmissionState.objects.first().is_open)

    def test_admission_view_existing_state(self):
        response = self.client.get(self.admission_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "http://example.com")

    def test_admission_state_model_str(self):
        self.assertEqual(str(self.admission), "Aberto")
        self.admission.is_open = False
        self.admission.save()
        self.assertEqual(str(self.admission), "Fechado")

    def test_admin_admission_state_display(self):
        admin_state = AdmissionState.objects.get(id=self.admission.id)
        self.assertEqual(admin_state.link_admission, "http://example.com")
