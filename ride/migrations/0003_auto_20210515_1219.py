# Generated by Django 3.1.6 on 2021-05-15 06:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0002_auto_20210321_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='acnonac',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='ride',
            name='money',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(5000)]),
        ),
    ]