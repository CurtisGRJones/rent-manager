# Generated by Django 4.0.4 on 2022-05-18 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='email',
            field=models.EmailField(default='default@default.ca', max_length=254),
            preserve_default=False,
        ),
    ]
