from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .forms import SimpleModelForm
from .models import SimpleModel


class SimpleModelTest(TestCase):
    def setUp(self):
        self.simple_model = SimpleModel.objects.create(name="Test Name", description="Test Description")

    def test_model_can_be_saved(self):
        self.assertEqual(SimpleModel.objects.count(), 1)

    def test_model_can_be_retrieved(self):
        retrieved_model = SimpleModel.objects.get(name="Test Name")
        self.assertEqual(retrieved_model.description, "Test Description")

    def test_model_can_be_updated(self):
        self.simple_model.description = "Updated Description"
        self.simple_model.save()
        updated_model = SimpleModel.objects.get(name="Test Name")
        self.assertEqual(updated_model.description, "Updated Description")

    def test_model_can_be_deleted(self):
        self.simple_model.delete()
        self.assertEqual(SimpleModel.objects.count(), 0)


class SimpleModelListViewTest(APITestCase):
    def setUp(self):
        SimpleModel.objects.create(name="Test Name 1", description="Test Description 1")
        SimpleModel.objects.create(name="Test Name 2", description="Test Description 2")

    def test_view_returns_status_code_200(self):
        url = reverse('simple_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_returns_all_objects(self):
        url = reverse('simple_list')
        response = self.client.get(url)
        self.assertEqual(len(response.data), 2)


class SimpleModelFormTest(TestCase):
    def test_form_is_valid_with_correct_data(self):
        form = SimpleModelForm(data={'name': 'Valid Name', 'description': 'Valid Description'})
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_with_incorrect_data(self):
        form = SimpleModelForm(data={'name': '', 'description': 'Valid Description'})
        self.assertFalse(form.is_valid())


class SimpleModelDetailViewTest(APITestCase):
    def setUp(self):
        self.simple_model = SimpleModel.objects.create(name="Test Name", description="Test Description")
        self.url = reverse('simple_detail', kwargs={'pk': self.simple_model.pk})

    def test_update_view_returns_status_code_200(self):
        response = self.client.put(self.url, {'name': 'Updated Name', 'description': 'Updated Description'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_view_updates_object(self):
        self.client.put(self.url, {'name': 'Updated Name', 'description': 'Updated Description'}, format='json')
        updated_model = SimpleModel.objects.get(pk=self.simple_model.pk)
        self.assertEqual(updated_model.name, 'Updated Name')

    def test_delete_view_returns_status_code_302(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_view_deletes_object(self):
        self.client.delete(self.url)
        self.assertEqual(SimpleModel.objects.count(), 0)
