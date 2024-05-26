import random
from django.core.management.base import BaseCommand
from map.models import Cities_Ly

class Command(BaseCommand):
    help = 'Generates vehicle objects in the database'

    def handle(self, *args, **options): 
        # random.Any,
        NUM_VEHICLES_TO_GENERATE = 5
        for _ in range(NUM_VEHICLES_TO_GENERATE):
            Cities_Ly.objects.create(
                latitude = random.uniform(44,47),
                longitude= random.uniform(-100,-80)
            )
        print(f"{Cities_Ly.objects.count()} Cities_Ly now in the database")    
    