from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError


def validate_description(value):
    if len(value) < 10:
        raise ValidationError('Не может быть короче 20 символов')

class EducationModel(models.Model):
    order = models.PositiveIntegerField(unique=True, verbose_name='Порядковый номер', validators=[MinValueValidator(1)])
    title = models.CharField(max_length=200, verbose_name='Название', validators=[MinLengthValidator(5)])
    description = models.TextField(verbose_name='Описание', validators=[validate_description])

    class Meta:
        ordering = ['order']
        verbose_name = 'Образовательный модуль'
        verbose_name_plural = 'Образовательные модули'

    def __str__(self):
        return self.title

