# Generated by Django 5.1.6 on 2025-04-09 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default=1234567, max_length=255),
            preserve_default=False,
        ),
    ]
