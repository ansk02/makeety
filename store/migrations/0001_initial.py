# Generated by Django 3.2.4 on 2021-06-17 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, unique=True, verbose_name='Produit')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('price', models.FloatField(default=0.0, verbose_name='Prix')),
                ('images', models.ImageField(upload_to='photos/produits')),
                ('stock', models.IntegerField(default=0)),
                ('is_available', models.BooleanField(default=True, verbose_name='Disponible')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Dernière modification')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
