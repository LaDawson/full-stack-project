# Generated by Django 3.0.8 on 2020-08-03 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0002_auto_20200803_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='consultation_cost',
            field=models.DecimalField(decimal_places=2, default=30, max_digits=5),
        ),
    ]
