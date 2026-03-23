from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import backend_view, WaterLevelReadingViewSet, SensorStationViewSet

router = DefaultRouter()
router.register(r'readings', WaterLevelReadingViewSet, basename='waterlevelreading')
router.register(r'stations', SensorStationViewSet, basename='sensorstation')

urlpatterns = [
    path('', backend_view, name='api-root'),
    path('', include(router.urls)),
]