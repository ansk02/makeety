# Generated by Django 3.2.4 on 2021-06-17 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=60, unique=True, verbose_name='Prenom')),
                ('last_name', models.CharField(max_length=60, unique=True, verbose_name='Nom')),
                ('username', models.CharField(max_length=25, unique=True, verbose_name='Pseudo')),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('city', models.CharField(blank=True, max_length=200, verbose_name='Ville')),
                ('phone_number', models.CharField(max_length=60, unique=True, verbose_name='Téléphone')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Creation')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='Dernière connexion')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'COMPTE PERSONNALISE',
                'verbose_name_plural': 'COMPTE PERSONNALISE',
            },
        ),
    ]
