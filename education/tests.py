from django.urls import reverse
from rest_framework.test import APITestCase

from .models import EducationModel
from .serializers import EducationalModuleSerializer


class EducationalModuleTests(APITestCase):
    def setUp(self):
        self.module = EducationModel.objects.create(
            order=1, title="Основы Python", description="Изучаем базовый синтаксис"
        )
        self.valid_data = {
            "order": 2,
            "title": "Объектно-ориентированное программирование",
            "description": "Изучение классов и объектов ООП, наследование",
        }
        self.invalid_data = {
            "order": "не число",  # Неправильный тип
            "title": "",  # Пустое поле
            "description": None,  # Null значение
        }

    def test_model_creation(self):
        """Тестирование создания модели"""
        self.assertEqual(EducationModel.objects.count(), 1)
        self.assertEqual(str(self.module), "Основы Python")

    def test_model_validation(self):
        """Тестирование валидации модели"""
        from django.core.exceptions import ValidationError

        invalid_module = EducationModel(order=None, title=None, description=None)
        with self.assertRaises(ValidationError):
            invalid_module.full_clean()

    # 2. Тесты сериализатора
    def test_serializer_valid_data(self):
        """Тестирование сериализатора с валидными данными"""
        serializer = EducationalModuleSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid_data(self):
        """Тестирование сериализатора с невалидными данными"""
        serializer = EducationalModuleSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(len(serializer.errors), 3)  # Ошибки для всех полей

    # 3. Тесты API (CRUD)
    def test_module_creation(self):
        url = reverse("modules-list")
        response = self.client.post(
            url,
            {
                "order": 2,
                "title": "Объектно-ориентированное программирование",
                "description": "Изучение классов и объектов ООП, наследование",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)

    def test_module_list(self):
        url = reverse("modules-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_module_update(self):
        url = reverse("modules-detail", args=[self.module.id])
        response = self.client.patch(url, {"title": "Python Basics"}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Python Basics")

    def test_module_deletion(self):
        url = reverse("modules-detail", args=[self.module.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(EducationModel.objects.count(), 0)

    def test_invalid_creation(self):
        """Тестирование обработки невалидных данных"""
        url = reverse("modules-list")  # Убедитесь, что имя URL правильное
        response = self.client.post(url, self.invalid_data, format="json")
        self.assertEqual(response.status_code, 400)
