# Generated by Django 3.0.7 on 2020-06-14 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScoringSystem', '0004_auto_20200613_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Name_cl',
            field=models.CharField(max_length=50, verbose_name="Ім'я:"),
        ),
        migrations.AlterField(
            model_name='client',
            name='Nomer_passport',
            field=models.CharField(max_length=50, verbose_name='Номер паспорту:'),
        ),
        migrations.AlterField(
            model_name='client',
            name='Po_batk_cl',
            field=models.CharField(max_length=50, verbose_name='По-батькові:'),
        ),
        migrations.AlterField(
            model_name='client',
            name='Seria_passport',
            field=models.CharField(max_length=50, verbose_name='Серія паспорту:'),
        ),
        migrations.AlterField(
            model_name='client',
            name='Surname_cl',
            field=models.CharField(max_length=50, verbose_name='Прізвище:'),
        ),
    ]
