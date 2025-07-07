from rest_framework import serializers
from .models import EducationModel

class EducationalModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationModel
        fields = ['order', 'title', 'description']
