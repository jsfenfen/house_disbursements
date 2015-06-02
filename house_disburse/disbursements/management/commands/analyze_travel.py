from disbursements.models import Expenditure, Summary
from datetime import date
from django.db.models import Sum, Count, Q

from django.core.management.base import BaseCommand, CommandError


quarter_list = ['2014Q1', '2014Q2', '2014Q3', '2014Q4']
class Command(BaseCommand):
    help = "look at travel summary, line items, and overall spending"
    requires_model_validation = False
    
    def handle(self, *args, **options):
        for quarter in quarter_list:
            bioguides = Summary.objects.filter(quarter=quarter).order_by('bioguide_id').values('bioguide_id').distinct()
            for bioguide in bioguides:
                if bioguide['bioguide_id']:
                    this_id = bioguide['bioguide_id']
                    
                    # get travel total:
                    travel_total = Summary.objects.filter(quarter=quarter, bioguide_id=this_id, category='TRAVEL').values('amount')
                    total = Summary.objects.filter(quarter=quarter, bioguide_id=this_id).values('amount')
                    print "quarter=%s travel=%s bioguide_id=%s" % (quarter, this_id, travel_total)