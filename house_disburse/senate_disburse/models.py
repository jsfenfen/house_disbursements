from django.db import models
from disbursements.models import clean_numeric

from dateutil.parser import parse as dateparse
from nameparser import HumanName

class first_name(models.Model):
    first_name = models.CharField(max_length=127, blank=True, null=True)
    country_code = models.CharField(max_length=2, blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    probability = models.FloatField(null=True)
    count = models.IntegerField(null=True)
    


class sod(models.Model):
    bioguide_id = models.CharField(max_length=7, blank=True, null=True, help_text="blank for now")
    source_doc = models.CharField(max_length=15, blank=True, null=True)
    senator_flag = models.CharField(max_length=1, blank=True, null=True)
    senator_name = models.CharField(max_length=127, blank=True, null=True)
    raw_office= models.CharField(max_length=256, blank=True, null=True)
    funding_year = models.CharField(max_length=7, blank=True, null=True)
    fiscal_year= models.CharField(max_length=7, blank=True, null=True)
    congress_no = models.CharField(max_length=3, blank=True, null=True)
    reference_page = models.CharField(max_length=5, blank=True, null=True)
    transaction_id = models.CharField(max_length=15, blank=True, null=True)
    date_posted_raw = models.CharField(max_length=15, blank=True, null=True)
    start_date_raw = models.CharField(max_length=15, blank=True, null=True)
    end_date_raw = models.CharField(max_length=15, blank=True, null=True)
    date_posted = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    salary_flag = models.CharField(max_length=1, blank=True, null=True)
    amount = models.FloatField(null=True)
    amount_raw = models.CharField(max_length=31, blank=True, null=True)
    payee = models.CharField(max_length=511, blank=True, null=True)
    
    payee_first = models.CharField(max_length=127, blank=True, null=True)
    payee_middle = models.CharField(max_length=127, blank=True, null=True)
    payee_last = models.CharField(max_length=127, blank=True, null=True)
    
    first_name = models.ForeignKey(first_name, null=True)
    
    def set_name(self):
        
        fixedname = self.payee
        nameparts = fixedname.split(",")
        if len(nameparts)==2:
            fixedname = nameparts[1] + " " + nameparts[0]
        
        name = HumanName(fixedname)
        
        if name:
            self.payee_first = name.first
            self.payee_middle = name.middle
            self.payee_last = name.last
            self.save()
        
        
    def set_data(self):
        try:
            self.amount = float(clean_numeric(self.amount_raw))
        except:
            print "Couldn't convert amount: %s" % (self.amount_raw)
            
            
        if self.start_date_raw:
            self.start_date = dateparse(self.start_date_raw)
        if self.end_date_raw:
            self.end_date = dateparse(self.end_date_raw)
        if self.date_posted_raw:
            self.date_posted = dateparse(self.date_posted_raw)
        
        
            
        
        self.save()
"""
# to make this tractable--albeit inefficient--index the file on years, then run this: 

from senate_disburse.models import *
more_results = True
numqueries = 0
while more_results:
 numqueries += 1
 print "got %s" % (numqueries * 100)
 es = sod.objects.filter(amount__isnull=True)[:100]
 if es:
  for e in es:
   e.set_data()
 else:
  more_results = False
"""

"""
from senate_disburse.models import sod
all_salaries = sod.objects.filter(salary_flag='1')
for a in all_salaries:
    a.set_name()
"""