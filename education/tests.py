from django.urls import reverse
from rest_framework.test import APITestCase
from .models import EducationModel

class EducationalModuleTests(APITestCase):
    def setUp(self):
        self.module = EducationModel.objects.create(
            order=1,
            title="Основы Python",
            description="Изучаем базовый синтаксис"
        )

    def test_module_creation(self):
        response = self.client.post('/api/modules/', {
            'order': 2,
            'title': "ООП",
            'description': "Классы и объекты"
        })
        self.assertEqual(response.status_code, 201)

    def test_module_list(self):
        response = self.client.get('/api/modules/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_module_update(self):
        url = reverse('educationalmodule-detail', args=[self.module.id])
        response = self.client.patch(url, {'title': "Python Basics"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], "Python Basics")

    def test_module_deletion(self):
        url = reverse('educationalmodule-detail', args=[self.module.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(EducationModel.objects.count(), 0)
