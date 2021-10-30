# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AnsimDataset(models.Model):
	
    lat = models.FloatField(null=False, max_length=300)
    lon = models.FloatField(null=False, max_length=300)
    ansimseq = models.IntegerField(null=False, primary_key=True)
    statecode = models.IntegerField(blank=True, null=True)
    statename = models.TextField(blank=True, null=True)
    wardname= models.TextField(blank=True, null=True)
    workplacename= models.TextField(blank=True, null=True)
    owner= models.TextField(blank=True, null=True)
    ansimdate=models.DateField(blank=True, null=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    category= models.TextField(blank=True, null=True)
    categorydetail= models.TextField(blank=True, null=True)
    tel= models.TextField(blank=True, null=True)
    isansim = models.TextField(blank=True, null=True)
    cancledate = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    modifydate = models.DateField(blank=True, null=True)
	
	
class PublicPDataset(models.Model):
	
	lat = models.FloatField(null=True, max_length=300)
	lon = models.FloatField(null=True, max_length=300)	
	ppid = models.TextField(blank=True, null=True)
	ppname = models.TextField(blank=True, null=True)
	ppcategory = models.TextField(blank=True, null=True)
	ppcase = models.TextField(blank=True, null=True)
	ppaddress1 = models.TextField(blank=True, null=True)
	ppaddress2 = models.TextField(blank=True, null=True)
	ppnum = models.IntegerField(blank=True, null=True)
	gpgi = models.TextField(blank=True, null=True)
	isdaysystem = models.TextField(blank=True, null=True)
	opdays = models.TextField(blank=True, null=True)
	wstime = models.DateField(blank=True, null=True)
	wetime = models.DateField(blank=True, null=True)
	sstime = models.DateField(blank=True, null=True)
	setime = models.DateField(blank=True, null=True)
	hstime = models.DateField(blank=True, null=True)
	hetime = models.DateField(blank=True, null=True)
	isfree = models.TextField(blank=True, null=True)
	baseptime = models.IntegerField(blank=True, null=True)
	basepfee = models.IntegerField(blank=True, null=True)
	addutime = models.IntegerField(blank=True, null=True)
	addifee = models.IntegerField(blank=True, null=True)
	daypathtime = models.IntegerField(blank=True, null=True)
	daypathfee = models.IntegerField(blank=True, null=True)
	monthpathfee = models.IntegerField(blank=True, null=True)
	paymeth = models.TextField(blank=True, null=True)
	note = models.TextField(blank=True, null=True)
	managementname = models.TextField(blank=True, null=True)
	tel = models.TextField(blank=True, null=True)
	modifydate = models.DateField(blank=True, null=True)
	agencycode = models.TextField(blank=True, null=True)
	agencyname = models.TextField(blank=True, null=True)
	dnote = models.TextField(blank=True, null=True)
	
	
	
	
	
	