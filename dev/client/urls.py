from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, TopRiskClients

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
urlpatterns = [
    path('', include(router.urls)),
    path('risk/', TopRiskClients.as_view())
]
