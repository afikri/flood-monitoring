# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import viewsets, permissions, serializers
from .models import SensorStation, WaterLevelReading
from .serializers import SensorStationSerializer, WaterLevelReadingSerializer


class WaterLevelReadingViewSet(viewsets.ModelViewSet):
    queryset = WaterLevelReading.objects.all()
    serializer_class = WaterLevelReadingSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        station_id = self.request.data.get('station')
        if not SensorStation.objects.filter(id=station_id).exists():
            raise serializers.ValidationError({"station": "Invalid Station ID"})
        serializer.save()


class SensorStationViewSet(viewsets.ModelViewSet):
    queryset = SensorStation.objects.all()
    serializer_class = SensorStationSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['GET'])
def backend_view(request, format=None):
    return Response({
        'readings': reverse('waterlevelreading-list', request=request, format=format),
        'stations': reverse('sensorstation-list', request=request, format=format),
    })