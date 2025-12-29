from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connections

class Command(BaseCommand):
    help = 'Test djongo MongoDB connection.'

    def handle(self, *args, **options):
        try:
            db_conn = connections['default']
            db = db_conn.connection
            self.stdout.write(self.style.SUCCESS(f"Connected to MongoDB database: {db.name}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"MongoDB connection failed: {e}"))
