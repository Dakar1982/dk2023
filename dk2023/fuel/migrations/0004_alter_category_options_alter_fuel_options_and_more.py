# Generated by Django 4.2.1 on 2023-06-15 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0003_alter_fuel_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Rodzaj paliwa', 'verbose_name_plural': 'Rodzaj paliwa'},
        ),
        migrations.AlterModelOptions(
            name='fuel',
            options={'verbose_name': 'Stacje i Cene', 'verbose_name_plural': 'Lista stacji'},
        ),
        migrations.AddField(
            model_name='fuel',
            name='status',
            field=models.CharField(choices=[('d', 'Dostępna'), ('n', 'Niedostępna')], default='d', max_length=1),
        ),
    ]
