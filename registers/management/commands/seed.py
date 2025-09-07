from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding database...'))
        # Seeding logic will go here in Stage 1
        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))
