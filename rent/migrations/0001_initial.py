# Generated by Django 4.0.4 on 2022-05-18 04:15

from django.db import migrations, models
import django.db.models.deletion
import packages.django_localflavor.localflavor.ca.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=16)),
                ('provence', packages.django_localflavor.localflavor.ca.models.CAProvinceField(max_length=2)),
                ('postal_code', packages.django_localflavor.localflavor.ca.models.CAPostalCodeField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_address', models.CharField(max_length=64)),
                ('unit', models.CharField(max_length=10)),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rent.property')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=16)),
                ('last_name', models.CharField(max_length=16)),
                ('current', models.BooleanField()),
                ('rent', models.DecimalField(decimal_places=2, max_digits=7)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('apartment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rent.unit')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_name', models.CharField(max_length=33)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('day_due', models.IntegerField()),
                ('tenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rent.tenant')),
            ],
        ),
    ]