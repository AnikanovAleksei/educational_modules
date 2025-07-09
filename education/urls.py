from django.urls import include, path
from rest_framework.routers import DefaultRouter

from education.views import EducationalModuleViewSet

router = DefaultRouter()
router.register(r"modules", EducationalModuleViewSet, basename="modules")

urlpatterns = [
    path("", include(router.urls)),
]
