# Generated by Django 2.2.5 on 2020-04-10 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20200410_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worksheet',
            name='ca_date',
            field=models.DateField(null=True, verbose_name='Fecha CA'),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='claim_date',
            field=models.DateField(null=True, verbose_name='Fecha reclamo pendientes'),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='pendings_date',
            field=models.DateField(null=True, verbose_name='Fecha SA'),
        ),
    ]