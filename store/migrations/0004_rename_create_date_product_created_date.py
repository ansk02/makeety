# Generated by Django 3.2.4 on 2021-06-19 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='create_date',
            new_name='created_date',
        ),
    ]
