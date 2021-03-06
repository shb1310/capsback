# Generated by Django 3.2.7 on 2021-10-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0011_auto_20211023_0515'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicpdataset',
            name='addifee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='addutime',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='agencycode',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='agencyname',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='basepfee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='baseptime',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='daypathfee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='daypathtime',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='gpgi',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='hetime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='hstime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='isdaysystem',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='isfree',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='lat',
            field=models.FloatField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='lon',
            field=models.FloatField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='managementname',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='modifydate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='monthpathfee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='opdays',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='paymeth',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='ppaddress1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='ppaddress2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='ppcase',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='ppcategory',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='ppid',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='ppname',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='ppnum',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='setime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='sstime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='tel',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='wetime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicpdataset',
            name='wstime',
            field=models.DateField(blank=True, null=True),
        ),
    ]
