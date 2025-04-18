# Generated by Django 5.1.6 on 2025-04-07 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemId', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('stockQuantity', models.IntegerField()),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('createdDate', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='item.item')),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('publicationYear', models.IntegerField()),
                ('isbn', models.CharField(max_length=13)),
                ('genre', models.CharField(max_length=100)),
            ],
            bases=('item.item',),
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='item.item')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=100)),
                ('ram', models.IntegerField()),
                ('storage', models.IntegerField()),
                ('screenSize', models.FloatField()),
            ],
            bases=('item.item',),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='item.item')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('operatingSystem', models.CharField(max_length=50)),
                ('ram', models.IntegerField()),
                ('storage', models.IntegerField()),
                ('cameraResolution', models.CharField(max_length=50)),
            ],
            bases=('item.item',),
        ),
    ]
