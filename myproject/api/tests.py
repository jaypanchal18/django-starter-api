import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import YourModel

class YourModelAPITests(APITestCase):
    def setUp(self):
        self.valid_payload = {
            'field1': 'value1',
            'field2': 'value2',
        }
        self.invalid_payload = {
            'field1': '',
            'field2': 'value2',
        }
        self.model_instance = YourModel.objects.create(**self.valid_payload)

    def test_create_model(self):
        response = self.client.post(reverse('yourmodel-list'), data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(YourModel.objects.count(), 2)

    def test_create_model_invalid(self):
        response = self.client.post(reverse('yourmodel-list'), data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_model(self):
        response = self.client.get(reverse('yourmodel-detail', args=[self.model_instance.id]), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['field1'], self.model_instance.field1)

    def test_update_model(self):
        response = self.client.put(reverse('yourmodel-detail', args=[self.model_instance.id]), data=json.dumps({'field1': 'new_value1'}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.model_instance.refresh_from_db()
        self.assertEqual(self.model_instance.field1, 'new_value1')

    def test_delete_model(self):
        response = self.client.delete(reverse('yourmodel-detail', args=[self.model_instance.id]), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(YourModel.objects.count(), 0)