# Generated by Django 4.2.6 on 2023-11-04 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_inventory_costperunit'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='salesPrice',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]