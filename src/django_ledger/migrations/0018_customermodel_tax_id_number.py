# Generated by Django 5.0.1 on 2024-06-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ledger', '0017_vendormodel_sales_tax_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermodel',
            name='tax_id_number',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Tax Registration Number'),
        ),
    ]
