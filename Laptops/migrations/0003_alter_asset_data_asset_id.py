# Generated by Django 4.1.3 on 2023-08-11 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Laptops', '0002_remove_asset_data_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset_data',
            name='asset_id',
            field=models.AutoField(auto_created=100, primary_key=True, serialize=False),
        ),
    ]
