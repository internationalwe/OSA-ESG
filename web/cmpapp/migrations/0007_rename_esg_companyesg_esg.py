# Generated by Django 3.2.8 on 2021-10-30 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmpapp', '0006_companyesg_esg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyesg',
            old_name='ESG',
            new_name='esg',
        ),
    ]
