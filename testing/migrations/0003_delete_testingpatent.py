# Generated by Django 4.1 on 2022-08-24 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestingPatent',
        ),
    ]