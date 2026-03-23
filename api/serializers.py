from rest_framework import serializers
from .models import SensorStation, WaterLevelReading

class WaterLevelReadingSerializer(serializers.ModelSerializer):
    """
    Converts WaterLevelReading models to JSON for IoT ingestion.
    to promote data interoperability
    """
    class Meta:
        model = WaterLevelReading
        fields = ['id', 'station', 'water_level', 'battery_pct', 'timestamp', 'status']
        # 'status' is read_only because backend calculates it (Data Integrity)
        read_only_fields = ['status', 'timestamp'] 

class SensorStationSerializer(serializers.ModelSerializer):
    """
    Converts SensorStation models to JSON for Dashboard visualization.
    """
    class Meta:
        model = SensorStation
        fields = ['id', 'station_id', 'name', 'latitude', 'longitude', 'alert_threshold']