# datahub/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Dataset

class DatasetModelTest(TestCase):
    def setUp(self):
        self.dataset = Dataset.objects.create(
            name="Test Dataset",
            description="A simple test dataset."
        )

    def test_dataset_creation(self):
        self.assertEqual(self.dataset.name, "Test Dataset")
        self.assertIsNotNone(self.dataset.created_at)

class DatasetViewsTest(TestCase):
    def setUp(self):
        Dataset.objects.create(name="View Test Dataset", description="Testing view response")

    def test_dataset_list_view(self):
        response = self.client.get(reverse('dataset-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test Dataset")

    def test_dataset_create_view(self):
        response = self.client.post(reverse('dataset-add'), {
            'name': 'New Dataset',
            'description': 'Dataset created through test'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Dataset.objects.filter(name='New Dataset').exists())
