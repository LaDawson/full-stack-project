# Generated by Django 3.0.8 on 2020-11-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0007_auto_20201110_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
