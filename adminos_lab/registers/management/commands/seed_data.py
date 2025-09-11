import datetime
from django.core.management.base import BaseCommand
from django.utils import timezone
from adminos_lab.registers.models import (
    Register, RegisterPage, TemperatureLog, CalibrationLog, WasteLog
)

class Command(BaseCommand):
    help = 'Seeds the database with initial data for registers and sample entries for today.'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')
        today = timezone.now().date()

        # Data for registers and their log entries
        seed_data = {
            'Temperature': {
                'logs': TemperatureLog,
                'entries': [
                    {'time': datetime.time(9, 0), 'location': 'Fridge-1', 'temperature': 4.5, 'initials': 'AB'},
                    {'time': datetime.time(13, 0), 'location': 'Fridge-1', 'temperature': 4.7, 'initials': 'AB'},
                ]
            },
            'Calibration': {
                'logs': CalibrationLog,
                'entries': [
                    {
                        'equipment_name': 'pH Meter', 'serial_no': 'SN12345', 'standard_used': 'pH 7.0 Buffer',
                        'result': 'Pass', 'tolerance': '±0.1', 'calibrated_by': 'CD', 'verified_by': 'EF'
                    },
                ]
            },
            'Waste': {
                'logs': WasteLog,
                'entries': [
                    {
                        'time': datetime.time(15, 30), 'yellow_bags_no': 5, 'yellow_bags_weight': 10.2,
                        'yellow_bags_labeled': True, 'sharps_containers_no': 2, 'sharps_containers_weight': 1.5,
                        'sharps_containers_labeled': True, 'handed_over_by': 'GH', 'vehicle_no': 'V54321',
                        'receiver_signature': 'Receiver Signature'
                    },
                ]
            }
        }

        for name, data in seed_data.items():
            # Get or create the register
            register, created = Register.objects.get_or_create(name=name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created register "{name}"'))
            else:
                self.stdout.write(f'Register "{name}" already exists.')

            # Get or create a register page for today
            page, created = RegisterPage.objects.get_or_create(register=register, date=today)
            if created:
                self.stdout.write(self.style.SUCCESS(f'  - Created page for {today}'))
            else:
                self.stdout.write(f'  - Page for {today} already exists.')

            # Create log entries for the page
            LogModel = data['logs']
            for entry_data in data['entries']:
                # Use get_or_create to ensure idempotency
                log_entry, created = LogModel.objects.get_or_create(page=page, **entry_data)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'    - Added {LogModel.__name__} entry.'))
                else:
                    self.stdout.write(f'    - {LogModel.__name__} entry already exists.')

        self.stdout.write(self.style.SUCCESS('Database seeding complete.'))
