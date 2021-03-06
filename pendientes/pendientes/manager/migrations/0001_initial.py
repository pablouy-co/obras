# Generated by Django 2.2.5 on 2020-04-17 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PendType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pend_type', models.CharField(max_length=50, verbose_name='Tipo de pendiente')),
            ],
        ),
        migrations.CreateModel(
            name='WorkSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=12, verbose_name='Sigla')),
                ('oppera', models.CharField(max_length=10, verbose_name='No. Oppera')),
                ('cs_date', models.DateField(null=True, verbose_name='Fecha CS')),
                ('cs_comments', models.CharField(blank=True, max_length=200, null=True, verbose_name='Comentarios sobre CS')),
                ('cs_pics_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='Fotos Supervision de obra')),
                ('pendings_date', models.DateField(blank=True, null=True, verbose_name='Fecha SA')),
                ('claim_date', models.DateField(blank=True, null=True, verbose_name='Fecha reclamo pendientes')),
                ('asp', models.CharField(blank=True, max_length=15, null=True, verbose_name='ASP responsable')),
                ('claim_pending_comments', models.CharField(blank=True, max_length=200, null=True, verbose_name='Cometarios sobre el reclamo a ASP')),
                ('ca_date', models.DateField(blank=True, null=True, verbose_name='Fecha CA')),
                ('ca_comments', models.CharField(blank=True, max_length=200, null=True, verbose_name='Comentarios sobre CA')),
                ('ca_pics_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='Fotos para servidor Antel')),
                ('closed', models.CharField(blank=True, choices=[('s', 'Si'), ('n', 'No')], default='n', max_length=1, verbose_name='Obra cerrada')),
                ('pend_type', models.ManyToManyField(blank=True, to='manager.PendType', verbose_name='Tipo de pendiente')),
            ],
            options={
                'ordering': ['oppera', 'site'],
            },
        ),
    ]
