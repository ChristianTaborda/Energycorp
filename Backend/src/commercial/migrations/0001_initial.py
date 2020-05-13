# Generated by Django 3.0.3 on 2020-05-13 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commercial',
            fields=[
                ('codeCommercial', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlCommercial', models.CharField(max_length=255)),
                ('nameCommercial', models.CharField(max_length=255)),
                ('contractorCommercial', models.CharField(max_length=255)),
                ('resourceCommercial', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommercialInvoice',
            fields=[
                ('codeCommercialInvoice', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commercial', models.ManyToManyField(related_name='commercials', to='commercial.Commercial')),
            ],
        ),
    ]
