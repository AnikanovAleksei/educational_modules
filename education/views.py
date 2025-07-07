from rest_framework import viewsets
from .models import EducationModel
from .serializers import EducationalModuleSerializer


class EducationalModuleViewSet(viewsets.ModelViewSet):
    queryset = EducationModel.objects.all()
    serializer_class = EducationalModuleSerializer
