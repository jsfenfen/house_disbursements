from django.db import models
from dateutil.parser import parse as dateparse


def clean_numeric(data):
    data = data.replace(",", "")
    return data



# Create your models here.
class Expenditure(models.Model):
    bioguide_id = models.CharField(max_length=7, blank=True, null=True)
    office = models.CharField(max_length=63, blank=True, null=True)
    quarter = models.CharField(max_length=7, blank=True, null=True)
    category = models.CharField(max_length=63, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    date_raw = models.CharField(max_length=15, blank=True, null=True)
    payee = models.CharField(max_length=63, blank=True, null=True)
    start_date_raw = models.CharField(max_length=15, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date_raw = models.CharField(max_length=15, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    purpose = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField(null=True)
    amount_raw = models.CharField(max_length=31, blank=True, null=True)
    year_raw = models.CharField(max_length=31, blank=True, null=True)
    year = models.IntegerField(null=True)
    transcode = models.CharField(max_length=31, blank=True, null=True)
    transcodelong = models.CharField(max_length=63, blank=True, null=True)
    recordid = models.CharField(max_length=31, blank=True, null=True)
    recip_orig= models.CharField(max_length=63, blank=True, null=True)
    
    def set_data(self):
        try:
            self.amount = float(clean_numeric(self.amount_raw))
        except:
            print "Couldn't convert amount: %s" % (self.amount_raw)
            
            
        if self.start_date_raw:
            self.start_date = dateparse(self.start_date_raw)
        if self.end_date_raw:
            self.end_date = dateparse(self.end_date_raw)
        
        
        try:
            year_raw = self.year_raw
            year_raw = year_raw.replace("FISCAL YEAR", "")
            year_raw = year_raw.strip()
            self.year = int(year_raw)
        except:
            print "couldn't convert year %s" % (self.year_raw)
            
        
        self.save()    
        
"""
# to make this tractable--albeit inefficient--index the file on years, then run this: 

from disbursements.models import *
more_results = True
numqueries = 0
while more_results:
    numqueries += 1
    print "got %s" % (numqueries * 100)
    es = Expenditure.objects.filter(year__isnull=True)[:100]
    if es:
        for e in es:
            e.set_data()
    else:
        more_results = False
"""


# Create your models here.
class Summary(models.Model):
    bioguide_id = models.CharField(max_length=7, blank=True, null=True)
    office = models.CharField(max_length=63, blank=True, null=True)
    year_raw = models.CharField(max_length=31, blank=True, null=True)
    year = models.IntegerField(null=True)
    quarter = models.CharField(max_length=7, blank=True, null=True)
    category = models.CharField(max_length=63, blank=True, null=True)
    amount = models.FloatField(null=True)
    amount_raw = models.CharField(max_length=31, blank=True, null=True)
    ytd = models.FloatField(null=True)
    ytd_raw = models.CharField(max_length=31, blank=True, null=True)
    
    def set_data(self):
        try:
            self.amount = float(clean_numeric(self.amount_raw))
        except:
            print "Couldn't convert amount: %s" % (self.amount_raw)
            
        
        try:
            self.ytd = float(clean_numeric(self.ytd_raw))
        except:
            print "Couldn't convert ytd amount: %s" % (self.ytd_raw)
        
        
        try:
            year_raw = self.year_raw
            year_raw = year_raw.replace("FISCAL YEAR", "")
            year_raw = year_raw.strip()
            self.year = int(year_raw)
        except:
            print "couldn't convert year %s" % (self.year_raw)
            
        
        self.save()


"""
# to make this tractable--albeit inefficient--index the file on years, then run this: 

from disbursements.models import *
more_results = True
numqueries = 0
while more_results:
    numqueries += 1
    print "got %s" % (numqueries * 100)
    es = Summary.objects.filter(year__isnull=True)[:100]
    if es:
        for e in es:
            e.set_data()
    else:
        more_results = False
"""

 