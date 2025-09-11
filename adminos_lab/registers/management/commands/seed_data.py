from django.core.management.base import BaseCommand
from django.utils import timezone
from adminos_lab.registers.models import Register, RegisterPage

class Command(BaseCommand):
    help = 'Seeds the database with initial data for registers.'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        # Create registers
        registers = ['Temperature', 'Calibration', 'Waste']
        for name in registers:
            register, created = Register.objects.get_or_create(name=name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created register "{name}"'))
            else:
                self.stdout.write(f'Register "{name}" already exists.')

            # Create a register page for today
            today = timezone.now().date()
            page, created = RegisterPage.objects.get_or_create(register=register, date=today)
            if created:
                self.stdout.write(self.style.SUCCESS(f'  - Created page for {today}'))
            else:
                self.stdout.write(f'  - Page for {today} already exists.')

        self.stdout.write(self.style.SUCCESS('Database seeding complete.'))
