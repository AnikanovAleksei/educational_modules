from django.urls import path, include
from rest_framework.routers import DefaultRouter
from education.views import EducationalModuleViewSet
from education.apps import EducationConfig

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'modules', EducationalModuleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]