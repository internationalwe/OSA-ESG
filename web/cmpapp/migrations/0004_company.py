# Generated by Django 3.2.8 on 2021-10-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmpapp', '0003_companylist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmp_ESG', models.CharField(max_length=10)),
                ('cmp_E', models.CharField(max_length=10)),
                ('cmp_S', models.CharField(max_length=10)),
                ('cmp_G', models.CharField(max_length=10)),
            ],
        ),
    ]
