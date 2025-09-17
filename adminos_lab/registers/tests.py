import pytest
from django.urls import reverse
from django.core.management import call_command
from django.utils import timezone
from .models import Register, RegisterPage, TemperatureLog, CalibrationLog, WasteLog

@pytest.mark.django_db
def test_health_check_returns_200(client):
    """
    Tests that the health check endpoint returns a 200 status code.
    """
    url = reverse('health_check')
    response = client.get(url)
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}

@pytest.mark.django_db
def test_seed_data_command(capsys):
    """
    Tests that the seed_data command populates the database with initial data.
    """
    # Run the seed_data command
    call_command('seed_data')

    # 1. Verify that registers exist
    assert Register.objects.count() == 3
    temp_reg = Register.objects.get(name='Temperature')
    calib_reg = Register.objects.get(name='Calibration')
    waste_reg = Register.objects.get(name='Waste')

    # 2. Verify that a RegisterPage exists for today
    today = timezone.now().date()
    assert RegisterPage.objects.filter(date=today).count() == 3

    temp_page = RegisterPage.objects.get(register=temp_reg, date=today)
    calib_page = RegisterPage.objects.get(register=calib_reg, date=today)
    waste_page = RegisterPage.objects.get(register=waste_reg, date=today)

    # 3. Verify that each log table has at least one row for today's page
    assert temp_page.temperature_logs.count() >= 2
    assert calib_page.calibration_logs.count() >= 1
    assert waste_page.waste_logs.count() >= 1

    # 4. Test idempotency: run the command again and check counts
    call_command('seed_data')
    assert Register.objects.count() == 3
    assert RegisterPage.objects.filter(date=today).count() == 3
    assert temp_page.temperature_logs.count() >= 2
    assert calib_page.calibration_logs.count() >= 1
    assert waste_page.waste_logs.count() >= 1
