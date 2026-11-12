"""Seed the store with the bundled catalogue the first time the app runs.

The fixture contains categories, products, specifications and trending
entries only (no users, orders or carts), so it is safe to load on a fresh
production database.
"""

from pathlib import Path

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction

from categories.models import Category
from products.models import Products

FIXTURE = Path(__file__).resolve().parents[2] / "fixtures" / "catalog.json"


class Command(BaseCommand):
    help = "Load the demo catalogue if the product table is empty."

    def handle(self, *args, **options):
        if Products.objects.exists() or Category.objects.exists():
            self.stdout.write("Catalogue already present, skipping seed.")
            return

        if not FIXTURE.exists():
            self.stdout.write(self.style.WARNING(f"Fixture not found: {FIXTURE}"))
            return

        with transaction.atomic():
            call_command("loaddata", str(FIXTURE), verbosity=0)

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {Products.objects.count()} products and "
                f"{Category.objects.count()} categories."
            )
        )
