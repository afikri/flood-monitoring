from django.db import models

class SensorStation(models.Model):
    """
    Represents an IoT Gateway (e.g., ESP32) deployed in the field.
    """
    station_id = models.CharField(max_length=50, unique=True, db_index=True)
    name = models.CharField(max_length=100)

    # Geospatial data for Leaflet map visualization
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    # Threshold logic for Early Warning (MHEWS experience)
    alert_threshold = models.DecimalField(max_digits=5, decimal_places=2)  # Meters
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.station_id})"

class WaterLevelReading(models.Model):
    """
    Ingested sensor data stream.
    """
    station = models.ForeignKey(SensorStation, on_delete=models.CASCADE, related_name='readings')
    water_level = models.DecimalField(max_digits=6, decimal_places=2)
    
    # IoT device health
    battery_pct = models.IntegerField(null=True, blank=True)  
    
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    
    # NORMAL or ALERT
    status = models.CharField(max_length=20, default='NORMAL')  

    def save(self, *args, **kwargs):
        # Server-side validation ensures data integrity 
        # Even if device sends wrong status, backend corrects it.
        if self.water_level >= self.station.alert_threshold:
            self.status = 'ALERT'
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['-timestamp']),
            models.Index(fields=['station', '-timestamp']),
        ]