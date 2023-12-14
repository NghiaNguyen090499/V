import csv
from django.core.management.base import BaseCommand
from noel.models import SubCategory, Product

class Command(BaseCommand):
    help = 'Load data from CSV into SubCategory and Product models'

    def handle(self, *args, **options):
        csv_file = 'noel.csv'  # Đường dẫn đến file CSV của bạn

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                subcategory, created = SubCategory.objects.get_or_create(
                    name=row['subcategory_name'],
                    defaults={'image': f'mycakes/images/{row["subcategory_image_name"]}'}
                )

                
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))