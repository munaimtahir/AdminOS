from django.db import models
from django.utils import timezone

class Register(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class RegisterPage(models.Model):
    register = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='pages')
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('register', 'date')

    def __str__(self):
        return f"{self.register.name} - {self.date}"

class TemperatureLog(models.Model):
    page = models.ForeignKey(RegisterPage, on_delete=models.CASCADE, related_name='temperature_logs')
    time = models.TimeField()
    location = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    initials = models.CharField(max_length=10)
    remarks = models.TextField(blank=True, null=True)

class CalibrationLog(models.Model):
    page = models.ForeignKey(RegisterPage, on_delete=models.CASCADE, related_name='calibration_logs')
    equipment_name = models.CharField(max_length=100)
    serial_no = models.CharField(max_length=100)
    standard_used = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    tolerance = models.CharField(max_length=50)
    calibrated_by = models.CharField(max_length=100)
    verified_by = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)

class WasteLog(models.Model):
    page = models.ForeignKey(RegisterPage, on_delete=models.CASCADE, related_name='waste_logs')
    time = models.TimeField()
    yellow_bags_no = models.PositiveIntegerField()
    yellow_bags_weight = models.DecimalField(max_digits=5, decimal_places=2)
    yellow_bags_labeled = models.BooleanField(default=False)
    sharps_containers_no = models.PositiveIntegerField()
    sharps_containers_weight = models.DecimalField(max_digits=5, decimal_places=2)
    sharps_containers_labeled = models.BooleanField(default=False)
    handed_over_by = models.CharField(max_length=100)
    vehicle_no = models.CharField(max_length=50)
    receiver_signature = models.CharField(max_length=100)
