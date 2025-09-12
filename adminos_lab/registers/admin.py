from django.contrib import admin
from .models import Register, RegisterPage, TemperatureLog, CalibrationLog, WasteLog

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(RegisterPage)
class RegisterPageAdmin(admin.ModelAdmin):
    list_display = ('register', 'date', 'created_at')
    search_fields = ('register__name', 'date')
    list_filter = ('date', 'register')

@admin.register(TemperatureLog)
class TemperatureLogAdmin(admin.ModelAdmin):
    list_display = ('page', 'time', 'location', 'temperature', 'initials')
    search_fields = ('page__register__name', 'location')
    list_filter = ('page__date',)

@admin.register(CalibrationLog)
class CalibrationLogAdmin(admin.ModelAdmin):
    list_display = ('page', 'equipment_name', 'serial_no', 'result', 'calibrated_by', 'verified_by')
    search_fields = ('equipment_name', 'serial_no')
    list_filter = ('page__date',)

@admin.register(WasteLog)
class WasteLogAdmin(admin.ModelAdmin):
    list_display = ('page', 'time', 'yellow_bags_no', 'yellow_bags_weight', 'handed_over_by')
    search_fields = ('handed_over_by',)
    list_filter = ('page__date',)
