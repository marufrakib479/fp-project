# Generated by Django 4.2.2 on 2023-08-17 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_tour', '0002_alter_tourpackagemodel_journey_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourpackagemodel',
            name='journey_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]