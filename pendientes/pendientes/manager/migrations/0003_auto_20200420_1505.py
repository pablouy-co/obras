# Generated by Django 2.2.5 on 2020-04-20 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_worksheet_pend_side'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worksheet',
            options={'ordering': ['cs_date', 'oppera']},
        ),
    ]