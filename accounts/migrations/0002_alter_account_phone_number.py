# Generated by Django 3.2.4 on 2021-06-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=60, verbose_name='Téléphone'),
        ),
    ]